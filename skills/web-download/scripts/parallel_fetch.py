#!/usr/bin/env python3
"""
并行网页内容获取工具

使用多线程并发下载多个网页内容。
"""

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse
import time


def fetch_url(url, timeout=30):
    """获取单个URL的内容"""
    try:
        # 这里应该使用实际的HTTP客户端
        # 例如：requests、httpx等
        # 由于这是框架代码，提供接口定义
        
        print(f"Fetching: {url}")
        
        # 模拟网络请求延迟
        time.sleep(0.1)
        
        # 返回结果应该包含：
        # - status: HTTP状态码
        # - content: 页面内容
        # - url: 最终URL（处理重定向后）
        
        return {
            "status": 200,
            "url": url,
            "content": f"Content from {url}",
            "success": True
        }
    except Exception as e:
        return {
            "status": 0,
            "url": url,
            "error": str(e),
            "success": False
        }


def load_urls(file_path):
    """从文件加载URL列表"""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    urls = []
    content = path.read_text(encoding='utf-8')
    
    for line in content.split('\n'):
        line = line.strip()
        if line and (line.startswith('http://') or line.startswith('https://')):
            urls.append(line)
    
    return urls


def sanitize_filename(url):
    """从URL生成安全的文件名"""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('.', '_')
    path = parsed.path.strip('/').replace('/', '_')
    
    if path:
        return f"{domain}_{path}"
    return domain


def main():
    parser = argparse.ArgumentParser(
        description="并行获取多个网页内容"
    )
    parser.add_argument("input", help="输入文件（每行一个URL）")
    parser.add_argument("-o", "--output", default="materials", help="输出目录")
    parser.add_argument("-t", "--threads", type=int, default=5, help="并发线程数")
    parser.add_argument("--timeout", type=int, default=30, help="请求超时时间（秒）")
    args = parser.parse_args()
    
    # 加载URL列表
    urls = load_urls(args.input)
    
    if not urls:
        print("No URLs found in input file")
        sys.exit(1)
    
    print(f"Found {len(urls)} URLs to fetch")
    print(f"Using {args.threads} threads")
    
    # 创建输出目录
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    # 并行获取
    success_count = 0
    fail_count = 0
    
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {
            executor.submit(fetch_url, url, args.timeout): url 
            for url in urls
        }
        
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                
                if result.get("success"):
                    # 保存内容
                    filename = sanitize_filename(result["url"])
                    output_file = output_dir / f"{filename}.md"
                    
                    content = f"# {result['url']}\n\n{result['content']}"
                    output_file.write_text(content, encoding='utf-8')
                    
                    success_count += 1
                    print(f"  ✓ Saved: {output_file.name}")
                else:
                    fail_count += 1
                    print(f"  ✗ Failed: {url} - {result.get('error', 'Unknown error')}")
                    
            except Exception as e:
                fail_count += 1
                print(f"  ✗ Error: {url} - {e}")
    
    print(f"\nComplete: {success_count} succeeded, {fail_count} failed")
    
    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
