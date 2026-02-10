# Vibe Writing Skill

Agent技能项目，用于agent进行vibe writing——基于主题调研和组织，编写详细、准确、完整、经过验证的文档。

## 项目概述

Vibe Writing是一套完整的agent技能流程，可基于用户输入的主题/概念/脑图，开展一步步的调研和组织，最终编写出包含参考资料、图表、图片链接的完整文档。

**适用场景**：
- 博客文章撰写
- 学习教程制作
- 科研论文写作
- 调研报告生成
- 技术文档编写

## 目录结构

```
vibe-writing-skill/
├── README.md
├── scripts/
│   ├── init_skill.py      # 初始化skill目录
│   └── package_skill.py   # 打包skill为.skill文件
├── skills/
│   ├── make-node-list/    # Skill 1: 拆解主题为节点列表
│   ├── web-download/      # Skill 2: 网络调研与材料下载
│   ├── process/           # Skill 3: 撰写节点内容
│   └── merge-all/         # Skill 4: 合并所有文档
└── dist/                  # 打包后的.skill文件输出目录
```

## 技能流程

### 1. make-node-list

**功能**：将用户输入的主题/知识树/脑图拆解为细粒度节点列表

**输入**：
- 主题关键词（如"机器学习基础"）
- 知识树/脑图结构
- 大纲框架

**输出**：`node-list.txt`
```
节点1内容
节点2内容
节点3内容
...
```

**特点**：
- 与用户沟通确定合适粒度
- 每个节点可独立完成（50-500字）
- 避免过粗或过细

### 2. web-download

**功能**：为每个节点进行网络调研和材料收集

**输入**：`node-list.txt`

**输出**：
- `materials/`目录：所有下载的资料
- `download.txt`：材料映射表
```
节点1内容: {节点1_材料1.md: URL1}, {节点1_材料2.md: URL2}
节点2内容: {节点2_材料1.md: URL1}, ...
```

**特点**：
- 多个子代理并行工作
- 深度检索网页/文章/文献
- 保存可验证、可追溯的材料

### 3. process

**功能**：为每个节点撰写完整的markdown文档

**输入**：`download.txt`

**输出**：每个节点一个独立的`{节点内容}.md`文件

**文档结构**：
- 概述
- 目录/脑图
- 正文内容
- 图表与可视化（Mermaid流程图）
- 在线图片URL
- 参考资料
- 相关链接

**特点**：
- 完整阅读所有本地材料
- 整合模型内化知识
- 生成详细、准确、完整的内容

### 4. merge-all

**功能**：合并所有节点文档为完整综合文档

**输入**：`node-list.txt` + 所有节点`.md`文件

**输出**：`{主标题}.md`完整文档

**处理内容**：
- 添加文档元数据（标题、时间、字数）
- 生成完整目录
- 润色节点间衔接
- 统一格式和术语
- 添加附录（参考资料、术语表）

## 使用方法

### 创建新技能

```bash
# 创建一个新的skill
python3 scripts/init_skill.py <skill-name> --path skills --resources scripts,references,assets
```

### 打包技能

```bash
# 打包skill为可分发的.skill文件
python3 scripts/package_skill.py skills/<skill-name> dist/
```

### 完整写作流程

1. **拆解主题**
   ```
   使用make-node-list skill，将主题拆解为节点列表
   ```

2. **收集材料**
   ```
   使用web-download skill，为每个节点收集参考资料
   ```

3. **撰写内容**
   ```
   使用process skill，并行撰写每个节点的内容
   ```

4. **合并文档**
   ```
   使用merge-all skill，合并所有节点为完整文档
   ```

## 示例

### 输入
```
主题：写一篇关于Docker的技术教程
```

### 流程
1. `make-node-list` → 生成10个节点
2. `web-download` → 收集30+篇资料
3. `process` → 生成10篇节点文档
4. `merge-all` → 合并为完整教程

### 输出
```markdown
# Docker完整技术教程

## 文档信息
- 字数统计：约8500字
- 章节数：10章

## 目录
...

(完整内容)

## 附录
- 参考资料列表
- 术语表
- 相关资源
```

## 技能规范

每个skill遵循以下规范：

### SKILL.md
- YAML frontmatter（name + description）
- 工作流程说明
- 使用示例
- 脚本说明
- 故障排除

### scripts/
- 可执行的Python/Bash脚本
- 模块化、可重用
- 包含完整注释

### references/
- 详细参考文档
- 仅在需要时加载
- 保持SKILL.md简洁

## 开发计划

- [ ] 添加更多输出格式支持（PDF、DOCX）
- [ ] 集成更多图表类型
- [ ] 支持多语言输出
- [ ] 添加质量评估工具
- [ ] 支持协作编辑模式

## 许可证

MIT License
