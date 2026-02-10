---
name: process
description: 撰写节点内容文档。读取download.txt，为每个节点整合本地材料并撰写详细、准确、完整的markdown文档。每个子代理并行处理一个节点，输出包含概述、目录/脑图、流程图、在线图片URL、参考资料的完整节点文档。适用于需要系统性、结构化内容创作的场景。
---

# Process

## Overview

为每个节点撰写完整的markdown文档。整合本地材料与模型内化知识，生成包含概述、目录、图表、图片链接、参考资料的详细内容。

## Workflow

### 1. 读取材料映射

从`download.txt`读取每个节点的材料文件列表。

### 2. 并行撰写策略

**启动多个子代理**（使用Task工具并行执行）：
- 每个子代理负责1个节点
- 根据节点数量动态调整子代理数量
- 建议同时运行3-6个子代理

### 3. 材料阅读与整合

**完整材料阅读**：
- 使用Read工具读取所有关联的materials文件
- 提取关键信息、数据、示例代码
- 整合不同来源的观点和方法
- 交叉验证信息的准确性

**信息提取清单**：
- [ ] 核心概念定义
- [ ] 关键技术原理
- [ ] 实践案例与代码
- [ ] 数据与统计信息
- [ ] 最佳实践建议
- [ ] 常见问题与解决方案

### 4. 文档结构要求

每个节点文档必须包含以下部分：

```markdown
# {节点标题}

## 概述
简短描述本节内容（2-3句话）

## 目录
或脑图/流程图

## 正文内容
详细、准确、完整的内容描述

## 图表与可视化
- 流程图（使用Mermaid语法）
- 架构图（使用Mermaid语法）
- 数据表格
- 在线图片URL

## 参考资料
列出所有引用来源

## 相关链接
扩展阅读资源
```

### 5. 输出格式

每个节点输出独立的markdown文件：
- 文件名：`{节点内容}.md`（使用node-list.txt中的节点名称）
- 编码：UTF-8
- 格式：标准Markdown（GitHub Flavored）

### 6. 内容质量标准

**详细程度**：
- 每个节点500-2000字
- 代码示例带注释
- 配置文件完整可用

**准确性**：
- 技术术语准确
- 代码可运行
- 版本信息明确

**完整性**：
- 覆盖核心知识点
- 包含实践环节
- 提供扩展资源

## Scripts

### `scripts/validate_document.py`

验证生成的文档是否符合质量标准。

**检查项**：
- 文档结构完整性
- 必需章节存在性
- Markdown格式正确性
- 图片链接有效性

### `scripts/word_count.py`

统计文档字数，确保内容充实。

## References

### `references/writing-guidelines.md`

详细的写作规范与风格指南。

参见[Writing Guidelines](references/writing-guidelines.md)获取：
- 标题层级规范
- 代码块格式要求
- 图片引用规范
- 参考文献格式

### `references/mermaid-cheatsheet.md`

Mermaid图表语法速查表。

参见[Mermaid Cheatsheet](references/mermaid-cheatsheet.md)获取：
- 流程图语法
- 时序图语法
- 状态图语法
- 类图语法

## Examples

### 示例：节点文档

**输入**：
- 节点：`React Hooks入门`
- 材料：`1_hooks_intro.md`, `1_hooks_guide.md`, `1_hooks_best_practices.md`

**输出** (`React Hooks入门.md`)：
```markdown
# React Hooks入门

## 概述

React Hooks是React 16.8引入的新特性，允许在函数组件中使用状态和其他React特性。Hooks解决了类组件的复杂性问题，提供了更简洁的代码组织方式。

## 目录

1. Hooks简介
2. useState Hook
3. useEffect Hook
4. 自定义Hooks
5. 最佳实践

## Hooks简介

### 什么是Hooks

Hooks是JavaScript函数，用于在函数组件中"钩入"React状态和生命周期特性。

### 为什么需要Hooks

- 解决类组件this指向问题
- 简化组件逻辑复用
- 更好的代码组织方式

## useState Hook

### 基本用法

\`\`\`jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>你点击了 {count} 次</p>
      <button onClick={() => setCount(count + 1)}>
        点击我
      </button>
    </div>
  );
}
\`\`\`

### 状态更新模式

| 模式 | 说明 | 示例 |
|------|------|------|
| 直接替换 | 简单类型 | `setCount(count + 1)` |
| 函数式更新 | 依赖旧值 | `setCount(prev => prev + 1)` |
| 对象更新 | 保留其他字段 | `setUser({...user, name: '新名字'})` |

## useEffect Hook

### 基本用法

\`\`\`jsx
useEffect(() => {
  // 副作用逻辑
  document.title = \`点击了 ${count} 次\`;

  return () => {
    // 清理函数
  };
}, [count]); // 依赖数组
\`\`\`

### 依赖数组规则

\`\`\`mermaid
graph TD
    A[useEffect] --> B{依赖数组}
    B -->|无| C[每次渲染都执行]
    B -->|空[]| D[仅挂载时执行]
    B -->|有值| E[依赖变化时执行]
\`\`\`

## 自定义Hooks

### 创建自定义Hook

\`\`\`jsx
function useWindowSize() {
  const [size, setSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight
  });

  useEffect(() => {
    const handleResize = () => {
      setSize({
        width: window.innerWidth,
        height: window.innerHeight
      });
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return size;
}
\`\`\`

![Hooks规则流程图](https://react.dev/learn/rules-of-hooks.png)

## 最佳实践

1. **只在最顶层使用Hooks**：不要在循环、条件或嵌套函数中调用
2. **只在React函数中调用**：在函数组件或自定义Hook中调用
3. **使用ESLint插件**：`eslint-plugin-react-hooks`自动检测违规

## 参考资料

- [React官方文档 - Hooks简介](https://react.dev/learn)
- [Hooks API索引](https://react.dev/reference/react)
- [Hooks常见问题](https://react.dev/reference/react/FAQ)

## 相关链接

- [React Hooks完整指南](https://www.runoob.com/reactjs/react-hooks.html)
- [Hooks最佳实践](https://blog.logrocket.com/guide-to-react-hooks/)
```

## Troubleshooting

| 问题 | 解决方案 |
|------|----------|
| 材料不足导致内容单薄 | 使用模型内化知识补充，保持客观 |
| 不同材料观点冲突 | 明确标注不同观点，保持中立 |
| 代码示例无法运行 | 验证代码完整性，添加环境说明 |
| 图片链接失效 | 使用稳定的官方资源URL |
| 文档结构不统一 | 参考标准模板检查 |

## Content Requirements

### 概述部分
- 2-3句话概括本节内容
- 说明本节在整体中的位置
- 预告本节将解决什么问题

### 正文内容
- 使用小标题组织内容
- 代码示例带注释
- 重要概念加粗强调
- 使用表格对比不同方案

### 图表与可视化
- 流程图使用Mermaid语法
- 架构图使用Mermaid graph语法
- 数据对比使用表格
- 截图使用在线URL（可从官方文档获取）

### 参考资料
- 使用标准引用格式
- 包含完整URL
- 按重要性排序
- 标注访问时间（可选）
