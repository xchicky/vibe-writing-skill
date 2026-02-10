# Vibe Writing - Agent使用指南

本文档为Agent提供使用Vibe Writing技能的完整指南。

## 快速开始

Vibe Writing是一套完整的文档写作流程，包含4个独立的skill，可以顺序或单独使用。

### 完整流程

```
用户主题 → make-node-list → web-download → process → merge-all → 完整文档
```

## 技能详解

### 1. make-node-list

**何时使用**：当用户提供一个主题、概念或知识树，需要将其拆解为可处理的小节点时。

**触发条件**：
- "写一篇关于X的文章"
- "制作X的教程"
- "将X拆解为章节"
- 提供了脑图或知识树结构

**输入**：
- 主题关键词（如"机器学习基础"）
- 知识树/脑图（Markdown或JSON格式）
- 大纲框架

**输出**：
- `node-list.txt` - 每行一个节点名称

**关键操作**：
```python
# 读取用户输入
# 分析主题复杂度
# 与用户沟通确定粒度
# 生成节点列表
```

**粒度参考**：
- 每个节点预期50-500字输出
- 节点之间相对独立
- 避免过于宽泛或过于琐碎

### 2. web-download

**何时使用**：当需要为每个节点收集参考资料时。

**触发条件**：
- 存在`node-list.txt`文件
- 需要为节点内容准备参考资料

**输入**：
- `node-list.txt`

**输出**：
- `materials/`目录 - 所有下载的资料
- `download.txt` - 节点到资料的映射

**关键操作**：
```python
# 读取node-list.txt
# 为每个节点进行网络搜索
# 使用web_reader获取完整内容
# 保存到materials/目录
```

**搜索策略**：
- 中英文双语搜索
- 官方文档优先
- 学术论文/技术博客
- 每节点至少2-3个资料来源

### 3. process

**何时使用**：当需要为每个节点撰写完整内容时。

**触发条件**：
- 存在`download.txt`文件
- 需要撰写节点内容

**输入**：
- `download.txt`
- `materials/`目录

**输出**：
- 多个`{节点名称}.md`文件

**关键操作**：
```python
# 读取download.txt获取材料列表
# 使用Read工具读取所有materials
# 整合材料+内化知识
# 按标准模板撰写节点文档
```

**文档结构**（必须包含）：
```markdown
# {节点标题}
## 概述
## 目录/脑图
## 正文内容
## 图表与可视化（Mermaid）
## 参考资料
## 相关链接
```

### 4. merge-all

**何时使用**：当需要将所有节点合并为完整文档时。

**触发条件**：
- 存在`node-list.txt`和多个节点.md文件
- 需要生成最终文档

**输入**：
- `node-list.txt`
- 所有节点.md文件

**输出**：
- `{主标题}.md`完整文档

**关键操作**：
```python
# 读取node-list.txt确定顺序
# 按顺序收集节点文档
# 添加文档元数据
# 生成完整目录
# 润色衔接
# 输出完整文档
```

## 并行处理策略

### web-download并行
```python
# 推荐3-6个并行子代理
# 每个子代理处理1-3个节点
# 使用Task工具并行执行
```

### process并行
```python
# 推荐3-6个并行子代理
# 每个子代理处理1个节点
# 独立撰写，互不干扰
```

## 文件约定

| 文件 | 格式 | 说明 |
|------|------|------|
| `node-list.txt` | 纯文本 | 每行一个节点名称 |
| `download.txt` | 纯文本 | `节点: {文件: URL}, ...` |
| `materials/` | 目录 | 存放所有参考资料 |
| `{节点}.md` | Markdown | 节点内容文档 |
| `{标题}.md` | Markdown | 最终完整文档 |

## 工作流示例

### 示例1：技术教程

```
用户: "写一篇Docker入门教程"

Agent操作:
1. make-node-list
   - 分析主题
   - 生成8-12个节点
   - 输出node-list.txt

2. web-download
   - 并行搜索资料
   - 保存30+篇材料
   - 输出download.txt

3. process
   - 并行撰写节点
   - 生成8-12个.md文件

4. merge-all
   - 合并为完整文档
   - 输出Docker入门教程.md
```

### 示例2：调研报告

```
用户: "调研大语言模型的幻觉问题"

Agent操作:
1. make-node-list
   - 生成学术论文结构
   - 包含摘要、方法、实验等

2. web-download
   - 搜索arxiv、论文网站
   - 收集10-20篇论文

3. process
   - 撰写学术风格内容
   - 包含引用、数据

4. merge-all
   - 生成调研报告.pdf格式
```

## 质量检查清单

### make-node-list
- [ ] 节点数量合理（5-20个）
- [ ] 每个节点粒度适中
- [ ] 节点之间逻辑清晰
- [ ] 用户已确认列表

### web-download
- [ ] 每个节点至少2个资料
- [ ] 资料来源权威可靠
- [ ] 材料已保存到materials/
- [ ] download.txt格式正确

### process
- [ ] 包含所有必需章节
- [ ] 有概述和参考资料
- [ ] 包含图表或代码示例
- [ ] 字数达标（500-2000字）

### merge-all
- [ ] 所有节点已包含
- [ ] 目录与章节对应
- [ ] 衔接自然流畅
- [ ] 格式统一规范

## 常见问题

**Q: 节点粒度如何把握？**
A: 参考每节点50-500字。不确定时使用AskUserQuestion与用户确认。

**Q: 某节点找不到资料怎么办？**
A: 尝试不同关键词组合，扩大搜索范围，或使用模型内化知识补充。

**Q: 如何保证内容准确性？**
A: 交叉验证多个资料来源，优先使用官方文档，明确标注不确定性。

**Q: 合并后格式混乱？**
A: 使用merge_documents.py脚本自动处理，或手动调整标题层级。

## 脚本工具

| 脚本 | 位置 | 用途 |
|------|------|------|
| generate_node_list.py | make-node-list/scripts/ | 从结构化输入生成节点列表 |
| parallel_fetch.py | web-download/scripts/ | 并行下载网页内容 |
| validate_document.py | process/scripts/ | 验证文档质量 |
| merge_documents.py | merge-all/scripts/ | 合并多个markdown文件 |
