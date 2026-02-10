# Vibe Writing Skills

本目录包含4个独立的agent skill，组成完整的Vibe Writing文档写作流程。

## 目录结构

```
skills/
├── make-node-list/     # 拆解主题为节点列表
├── web-download/       # 网络调研与材料下载
├── process/            # 撰写节点内容
└── merge-all/          # 合并所有文档
```

## 使用流程

### 完整工作流

```
主题 → make-node-list → node-list.txt
     ↓
     web-download → materials/ + download.txt
     ↓
     process → {节点}.md × N
     ↓
     merge-all → 完整文档.md
```

### 单独使用

每个skill也可以独立使用：

- **make-node-list**：用于任务分解、大纲生成
- **web-download**：用于资料收集、调研整理
- **process**：用于内容撰写、文档生成
- **merge-all**：用于文档合并、格式整理

## Skill详解

### make-node-list

将主题/概念/脑图拆解为细粒度节点列表。

**使用场景**：
- 文档大纲生成
- 任务分解规划
- 知识结构整理

**输入/输出**：
```
输入: 主题/知识树/脑图
输出: node-list.txt
```

**交互流程**：
1. 询问用户意图：博客/教程/论文/其他
2. 询问节点数量：5/10/15/20/agent决定/其他
3. 根据选择智能拆解主题

**文件**：
- `SKILL.md` - 技能说明
- `scripts/generate_node_list.py` - 节点列表生成工具

### web-download

为每个节点进行网络调研和材料收集。

**使用场景**：
- 参考资料收集
- 网页内容批量获取
- 调研材料整理

**输入/输出**：
```
输入: node-list.txt
输出: materials/目录 + download.txt
```

**文件**：
- `SKILL.md` - 技能说明
- `scripts/parallel_fetch.py` - 并行下载工具

### process

为每个节点撰写完整的markdown文档。

**使用场景**：
- 节点内容撰写
- 技术文档生成
- 教程章节编写

**输入/输出**：
```
输入: download.txt + materials/
输出: {节点}.md × N
```

**文件**：
- `SKILL.md` - 技能说明
- `scripts/validate_document.py` - 文档质量验证
- `references/writing-guidelines.md` - 写作规范
- `references/mermaid-cheatsheet.md` - 图表语法速查

### merge-all

将所有节点文档合并为完整的综合文档。

**使用场景**：
- 多文档合并
- 格式统一整理
- 最终文档生成

**输入/输出**：
```
输入: node-list.txt + {节点}.md × N
输出: 完整文档.md
```

**文件**：
- `SKILL.md` - 技能说明
- `scripts/merge_documents.py` - 文档合并工具

## 快速参考

### 触发词对照

| 用户需求 | 使用skill |
|----------|-----------|
| "写一篇关于X的文章" | make-node-list |
| "收集X的相关资料" | web-download |
| "撰写X的内容" | process |
| "合并所有章节" | merge-all |

### 文件格式

| 文件类型 | 格式 | 位置 |
|----------|------|------|
| 节点列表 | `.txt` | 项目根目录 |
| 材料映射 | `.txt` | 项目根目录 |
| 参考资料 | `.md/.txt` | `materials/`目录 |
| 节点文档 | `.md` | 项目根目录或指定目录 |
| 最终文档 | `.md` | 项目根目录 |

## 质量标准

### 节点列表
- 节点数量：5-20个
- 每节点预期：50-500字
- 逻辑清晰、相对独立

### 参考资料
- 每节点至少2-3个来源
- 优先官方文档和权威来源
- 材料完整可追溯

### 节点文档
- 包含概述、正文、参考资料
- 有图表或代码示例
- 字数500-2000字

### 最终文档
- 所有节点已包含
- 目录完整对应
- 格式统一规范
- 衔接自然流畅

## 脚本使用

### generate_node_list.py

```bash
# 从JSON生成节点列表
python3 skills/make-node-list/scripts/generate_node_list.py input.json

# 从Markdown大纲生成
python3 skills/make-node-list/scripts/generate_node_list.py outline.md
```

### parallel_fetch.py

```bash
# 并行下载URL列表
python3 skills/web-download/scripts/parallel_fetch.py urls.txt -o materials/

# 指定并发数
python3 skills/web-download/scripts/parallel_fetch.py urls.txt -t 10
```

### validate_document.py

```bash
# 验证单个文档
python3 skills/process/scripts/validate_document.py document.md

# 验证多个文档
python3 skills/process/scripts/validate_document.py *.md
```

### merge_documents.py

```bash
# 合并节点文档
python3 skills/merge-all/scripts/merge_documents.py \
  -n node-list.txt \
  -d nodes/ \
  -t "文档标题" \
  -o output.md
```

## 打包与分发

每个skill可以独立打包为`.skill`文件：

```bash
# 打包单个skill
python3 scripts/package_skill.py skills/make-node-list dist/

# 打包所有skill
for skill in skills/*/; do
  python3 scripts/package_skill.py "$skill" dist/
done
```

打包后的`.skill`文件可以直接安装到Claude Code使用。

## 参考资源

- [AGENTS.md](../AGENTS.md) - Agent使用指南
- [README.md](../README.md) - 项目概述
- 各skill的`SKILL.md` - 详细技能说明
