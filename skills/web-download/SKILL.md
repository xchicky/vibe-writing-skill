---
name: web-download
description: 为每个节点进行网络调研和材料下载。读取node-list.txt，开启多个子代理并行进行节点内容的网络调研，深度检索相关网页/文章/博客/文献，下载并保存到本地，输出download.txt文件记录每个节点的材料来源。适用于需要大量背景资料、数据验证、参考来源的文档写作场景。
---

# Web Download

## Overview

为`node-list.txt`中的每个节点进行网络调研，收集并保存可验证、可追溯的参考资料。多个子代理并行工作，每个子代理负责一个或多个节点的材料收集。

## Workflow

### 1. 读取节点列表

从`node-list.txt`读取待处理的节点列表。

### 2. 并行调研策略

**启动多个子代理**（使用Task工具并行执行）：
- 每个子代理处理1-3个节点
- 根据节点数量动态调整子代理数量
- 建议同时运行3-6个子代理以平衡效率与稳定性

### 3. 深度检索方法

**搜索策略**：
- 使用WebSearch工具进行多轮搜索
- 尝试不同的关键词组合
- 包含中英文双语搜索
- 针对技术内容搜索官方文档

**搜索关键词构建**：
```
基础搜索："{节点名称}"
详细搜索："{节点名称} 原理 教程"
技术搜索："{节点名称} implementation guide"
学术搜索："{节点名称} research paper"
```

### 4. 资料收集与保存

**目标资料类型**：
- 技术文档与官方指南
- 学术论文与研究报告
- 技术博客与教程
- 实践案例与代码示例

**保存规则**：
1. 创建`materials/`目录存储所有资料
2. 使用web_reader工具获取完整网页内容
3. 每个资料保存为独立文件，命名格式：`{节点索引}_{来源标识}.{ext}`
4. 支持的文件格式：
   - `.md` - Markdown格式内容
   - `.txt` - 纯文本内容
   - `.json` - 结构化数据

### 5. 输出格式

创建`download.txt`文件：
```
节点1内容: {节点1_材料1.md: 来源URL1}, {节点1_材料2.md: 来源URL2}
节点2内容: {节点2_材料1.md: 来源URL1}, {节点2_材料2.md: 来源URL2}
...
```

**文件命名规范**：
- 使用`{序号}_{简短描述}.{扩展名}`格式
- 序号与node-list.txt中的行号对应
- 简短描述反映资料主题

## Scripts

### `scripts/parallel_fetch.py`

并行下载工具，用于加速多个URL的内容获取。

**功能**：
- 并发下载多个网页
- 自动重试失败的请求
- 进度显示与错误报告

### `scripts/validate_sources.py`

验证资料完整性与可访问性。

**功能**：
- 检查已下载资料的完整性
- 验证URL的可访问性
- 生成资料质量报告

## Examples

### 示例：节点调研

**输入** (`node-list.txt`)：
```
React Hooks入门
Docker容器化技术
微服务架构设计
```

**搜索策略**：
```
节点1: React Hooks入门
- 搜索1: "React Hooks 入门教程"
- 搜索2: "React useState useEffect 官方文档"
- 搜索3: "React Hooks best practices"
```

**输出** (`download.txt`)：
```
React Hooks入门: {1_hooks_intro.md: https://react.dev/learn}, {1_hooks_guide.md: https://www.runoob.com/reactjs/react-hooks.html}, {1_hooks_best_practices.md: https://blog.logrocket.com/guide-to-react-hooks/}
Docker容器化技术: {2_docker_intro.md: https://docs.docker.com/get-started/}, {2_docker_tutorial.md: https://yeasy.gitbook.io/docker_practice/}
微服务架构设计: {3_microservices_patterns.md: https://microservices.io/patterns/}, {3_microservices_guide.md: https://martinfowler.com/articles/microservices.html}
```

## Materials目录结构

```
materials/
├── 1_hooks_intro.md
├── 1_hooks_guide.md
├── 1_hooks_best_practices.md
├── 2_docker_intro.md
├── 2_docker_tutorial.md
├── 3_microservices_patterns.md
└── 3_microservices_guide.md
```

## Troubleshooting

| 问题 | 解决方案 |
|------|----------|
| 某个节点找不到资料 | 尝试不同关键词，扩大搜索范围 |
| 网页内容无法获取 | 使用web_reader工具获取完整内容 |
| 资料质量不佳 | 优先选择官方文档、权威来源 |
| 并行请求失败 | 减少并发数，添加重试机制 |
| 资料重复 | 去重并合并相似内容 |

## Quality Standards

每个节点应收集：
- **至少2-3个高质量资料来源**
- **涵盖不同角度**（理论+实践）
- **优先级排序**：官方文档 > 权威教程 > 技术博客 > 个人笔记
- **时间要求**：优先选择近1-2年的资料（技术快速迭代领域）
