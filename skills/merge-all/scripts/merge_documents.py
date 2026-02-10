#!/usr/bin/env python3
"""
文档合并工具

将多个markdown节点文档合并为一个完整的文档。
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


def read_node_list(file_path):
    """读取节点列表"""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: node-list.txt not found: {file_path}")
        sys.exit(1)
    
    nodes = [line.strip() for line in path.read_text(encoding='utf-8').split('\n') if line.strip()]
    return nodes


def find_node_document(node_name, search_dir="."):
    """查找节点对应的markdown文件"""
    search_path = Path(search_dir)
    
    # 精确匹配
    exact_match = search_path / f"{node_name}.md"
    if exact_match.exists():
        return exact_match
    
    # 模糊匹配
    for md_file in search_path.glob("*.md"):
        if node_name in md_file.stem:
            return md_file
    
    return None


def generate_toc(content):
    """从内容生成目录"""
    toc = []
    lines = content.split('\n')
    
    for line in lines:
        # 匹配标题
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2)
            
            # 生成锚点
            anchor = text.lower()
            anchor = re.sub(r'[^\w\s-]', '', anchor)
            anchor = re.sub(r'[\s_]+', '-', anchor)
            
            # 生成目录项
            indent = "  " * (level - 1)
            toc.append(f"{indent}- [{text}](#{anchor})")
    
    return '\n'.join(toc)


def count_words(content):
    """统计字数"""
    clean_content = re.sub(r'[#*`\[\]()]', ' ', content)
    clean_content = re.sub(r'\s+', ' ', clean_content)
    return len(clean_content.strip().split())


def merge_nodes(node_list, node_dir, output_title):
    """合并节点文档"""
    merged_content = []
    missing_nodes = []
    
    # 收集所有节点内容
    all_content = ""
    
    for node in node_list:
        node_file = find_node_document(node, node_dir)
        
        if node_file is None:
            missing_nodes.append(node)
            continue
        
        node_content = node_file.read_text(encoding='utf-8')
        all_content += node_content + "\n\n"
    
    # 生成文档头部
    header = f"""# {output_title}

## 文档信息
- 创建时间：{datetime.now().strftime('%Y-%m-%d')}
- 节点数量：{len(node_list) - len(missing_nodes)}/{len(node_list)}
- 字数统计：约{count_words(all_content)}字

## 目录

{generate_toc(all_content)}

---

"""
    
    merged_content.append(header)
    
    # 添加各节点内容
    for node in node_list:
        node_file = find_node_document(node, node_dir)
        
        if node_file is None:
            continue
        
        node_content = node_file.read_text(encoding='utf-8')
        
        # 添加分隔符
        merged_content.append("\n\n---\n\n")
        merged_content.append(node_content)
    
    # 添加附录
    appendix = """

---

## 附录

### 完整参考资料

本文档内容基于以下资料整理编写，具体引用请参见各章节。

### 相关资源

- [Vibe Writing Skill](https://github.com/your-repo/vibe-writing-skill)
"""
    
    merged_content.append(appendix)
    
    # 报告缺失节点
    if missing_nodes:
        print(f"\n警告: 以下节点文档未找到:")
        for node in missing_nodes:
            print(f"  - {node}")
    
    return ''.join(merged_content)


def main():
    parser = argparse.ArgumentParser(
        description="合并多个节点markdown文档"
    )
    parser.add_argument("-n", "--node-list", default="node-list.txt", help="节点列表文件")
    parser.add_argument("-d", "--node-dir", default=".", help="节点文档目录")
    parser.add_argument("-o", "--output", help="输出文件名")
    parser.add_argument("-t", "--title", help="文档主标题")
    args = parser.parse_args()
    
    # 读取节点列表
    nodes = read_node_list(args.node_list)
    
    if not nodes:
        print("Error: No nodes found in node-list.txt")
        sys.exit(1)
    
    print(f"Found {len(nodes)} nodes to merge")
    
    # 确定输出文件名
    output_title = args.title or nodes[0] if nodes else "merged_document"
    output_file = args.output or f"{output_title}.md"
    
    # 合并文档
    merged = merge_nodes(nodes, args.node_dir, output_title)
    
    # 写入输出文件
    Path(output_file).write_text(merged, encoding='utf-8')
    
    print(f"\n合并完成: {output_file}")


if __name__ == "__main__":
    main()
