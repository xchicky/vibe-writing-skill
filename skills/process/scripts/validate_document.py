#!/usr/bin/env python3
"""
文档质量验证工具

检查生成的markdown文档是否符合质量标准。
"""

import re
import sys
from pathlib import Path


class DocumentValidator:
    """Markdown文档验证器"""
    
    REQUIRED_SECTIONS = [
        "概述", "目录", "参考资料"
    ]
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = ""
        self.errors = []
        self.warnings = []
        self.info = []
    
    def load(self):
        """加载文档内容"""
        if not self.file_path.exists():
            self.errors.append(f"文件不存在: {self.file_path}")
            return False
        
        self.content = self.file_path.read_text(encoding='utf-8')
        return True
    
    def check_structure(self):
        """检查文档结构"""
        lines = self.content.split('\n')
        
        # 检查是否有主标题
        if not self.content.startswith('#'):
            self.errors.append("缺少主标题（#）")
        
        # 检查必需章节
        for section in self.REQUIRED_SECTIONS:
            pattern = f"## {section}"
            if pattern not in self.content:
                self.errors.append(f"缺少必需章节: {section}")
        
        # 检查代码块是否有语言标识
        code_blocks = re.findall(r'```(\w*)', self.content)
        empty_lang_blocks = [b for b in code_blocks if b == '']
        if empty_lang_blocks:
            self.warnings.append(f"有 {len(empty_lang_blocks)} 个代码块缺少语言标识")
    
    def check_links(self):
        """检查链接格式"""
        # 检查Markdown链接格式
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        links = re.findall(link_pattern, self.content)
        
        for text, url in links:
            # 检查URL格式
            if url.startswith('http') and not url.startswith(('http://', 'https://')):
                self.errors.append(f"无效的URL格式: {url}")
    
    def check_images(self):
        """检查图片引用"""
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        images = re.findall(img_pattern, self.content)
        
        for alt, url in images:
            # 检查是否使用在线URL
            if not url.startswith(('http://', 'https://')):
                self.warnings.append(f"图片使用相对路径: {url}")
    
    def check_word_count(self):
        """统计字数"""
        # 移除markdown标记
        clean_content = re.sub(r'[#*`\[\]()]', ' ', self.content)
        clean_content = re.sub(r'\s+', ' ', clean_content)
        
        words = clean_content.strip().split()
        word_count = len(words)
        
        self.info.append(f"总字数: {word_count}")
        
        # 检查字数是否达标（假设最少500字）
        if word_count < 500:
            self.warnings.append(f"文档字数较少: {word_count} < 500")
    
    def validate(self):
        """执行所有验证"""
        if not self.load():
            return False
        
        self.check_structure()
        self.check_links()
        self.check_images()
        self.check_word_count()
        
        return True
    
    def report(self):
        """生成验证报告"""
        print(f"\n验证报告: {self.file_path.name}")
        print("=" * 50)
        
        if self.info:
            print("\n信息:")
            for item in self.info:
                print(f"  ℹ {item}")
        
        if self.warnings:
            print("\n警告:")
            for item in self.warnings:
                print(f"  ⚠ {item}")
        
        if self.errors:
            print("\n错误:")
            for item in self.errors:
                print(f"  ✗ {item}")
        
        print("\n" + "=" * 50)
        
        if self.errors:
            print("验证失败: 发现错误")
            return False
        elif self.warnings:
            print("验证通过: 存在警告")
            return True
        else:
            print("验证通过: 完全符合标准")
            return True


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_document.py <markdown_file> [markdown_file2...]")
        sys.exit(1)
    
    all_passed = True
    
    for file_path in sys.argv[1:]:
        validator = DocumentValidator(file_path)
        if validator.validate():
            if not validator.report():
                all_passed = False
        else:
            all_passed = False
    
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
