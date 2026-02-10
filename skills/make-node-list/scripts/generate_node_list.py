#!/usr/bin/env python3
"""
节点列表生成工具

从结构化输入（JSON、Markdown大纲等）自动生成节点列表。
"""

import json
import re
import sys
from pathlib import Path


def parse_json_tree(data, prefix="", results=None):
    """解析JSON格式的知识树"""
    if results is None:
        results = []
    
    if isinstance(data, dict):
        if "title" in data:
            title = data["title"]
            if "children" in data and data["children"]:
                # 有子节点，不添加父节点
                pass
            else:
                # 叶子节点，添加到结果
                results.append(f"{prefix}{title}".strip())
            
            # 递归处理子节点
            for child in data.get("children", []):
                parse_json_tree(child, f"{prefix}{title} - ", results)
    
    elif isinstance(data, list):
        for item in data:
            parse_json_tree(item, prefix, results)
    
    return results


def parse_markdown_outline(content):
    """解析Markdown格式的大纲"""
    results = []
    lines = content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # 跳过空行和标题行
            if re.match(r'^[\d\.\-\*]+\s+', line):
                # 移除列表标记
                clean_line = re.sub(r'^[\d\.\-\*]+\s+', '', line)
                if clean_line:
                    results.append(clean_line)
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_node_list.py <input_file> [output_file]")
        print("\nSupported formats:")
        print("  - JSON: Hierarchical tree structure")
        print("  - MD:   Markdown outline/list")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("node-list.txt")
    
    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)
    
    content = input_file.read_text(encoding='utf-8')
    results = []
    
    # 根据文件扩展名选择解析方式
    if input_file.suffix == '.json':
        try:
            data = json.loads(content)
            results = parse_json_tree(data)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}")
            sys.exit(1)
    elif input_file.suffix in ['.md', '.txt']:
        results = parse_markdown_outline(content)
    else:
        print(f"Error: Unsupported file format: {input_file.suffix}")
        sys.exit(1)
    
    if not results:
        print("Warning: No nodes generated from input")
    
    # 写入输出文件
    output_file.write_text('\n'.join(results), encoding='utf-8')
    
    print(f"Generated {len(results)} nodes")
    print(f"Output: {output_file}")


if __name__ == "__main__":
    main()
