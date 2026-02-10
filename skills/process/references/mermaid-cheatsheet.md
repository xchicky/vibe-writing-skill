# Mermaid Cheatsheet

## 流程图 (Flowchart)

### 方向
```mermaid
graph TD  # Top Down
graph LR  # Left Right
graph BT  # Bottom Top
graph RL  # Right Left
```

### 基本形状
```mermaid
graph TD
    A[矩形] --> B(圆角矩形)
    B --> C{菱形/判断}
    C --> D[/平行四边形/]
    C --> E[[圆柱体/数据库]]
    C --> F[(圆形)]
    C --> G>{{六边形}}
```

### 示例
```mermaid
graph TD
    A[开始] --> B{判断条件}
    B -->|是| C[操作1]
    B -->|否| D[操作2]
    C --> E[结束]
    D --> E
```

## 时序图 (Sequence Diagram)

### 基本语法
```mermaid
sequenceDiagram
    participant A as 用户
    participant B as 系统
    A->>B: 请求
    B-->>A: 响应
```

### 箭头类型
| 类型 | 语法 | 说明 |
|------|------|------|
| 实线 | `->` | 同步调用 |
| 虚线 | `-->` | 异步消息 |
| 实线带开叉 | `->>` | 返回消息 |
| 虚线带开叉 | `-->>` | 异步返回 |

### 示例
```mermaid
sequenceDiagram
    participant User as 用户
    participant Client as 客户端
    participant Server as 服务器

    User->>Client: 输入数据
    Client->>Server: 发送请求
    Server-->>Client: 返回结果
    Client-->>User: 显示结果
```

## 状态图 (State Diagram)

### 基本语法
```mermaid
stateDiagram-v2
    [*] --> 状态1
    状态1 --> 状态2: 事件
    状态2 --> [*]
```

### 示例
```mermaid
stateDiagram-v2
    [*] --> 待处理
    待处理 --> 处理中: 开始处理
    处理中 --> 已完成: 处理成功
    处理中 --> 失败: 处理失败
    失败 --> 待处理: 重试
    已完成 --> [*]
    失败 --> [*]
```

## 类图 (Class Diagram)

### 基本语法
```mermaid
classDiagram
    class ClassName {
        +publicField
        -privateField
        #protectedField
        +publicMethod()
        -privateMethod()
    }
```

### 关系类型
| 类型 | 语法 |
|------|------|
| 继承 | `<|--` |
| 组合 | `*--` |
| 聚合 | `o--` |
| 关联 | `-->` |
| 依赖 | `..>` |

### 示例
```mermaid
classDiagram
    class Animal {
        +String name
        +eat()
        +sleep()
    }
    class Dog {
        +bark()
    }
    class Cat {
        +meow()
    }
    Animal <|-- Dog
    Animal <|-- Cat
```

## 实体关系图 (ER Diagram)

### 基本语法
```mermaid
erDiagram
    ENTITY1 {
        type property
    }
    ENTITY2 {
        type property
    }
    ENTITY1 ||--o{ ENTITY2 : relationship
```

### 示例
```mermaid
erDiagram
    User {
        int id PK
        string name
        string email
    }
    Post {
        int id PK
        string title
        text content
    }
    User ||--o{ Post : "writes"
```

## 甘特图 (Gantt Chart)

### 基本语法
```mermaid
gantt
    title 项目计划
    dateFormat  YYYY-MM-DD
    section 阶段1
    任务1 :a1, 2024-01-01, 7d
    任务2 :after a1, 5d
```

### 示例
```mermaid
gantt
    title 开发计划
    dateFormat  YYYY-MM-DD
    section 需求分析
    需求调研    :done, des1, 2024-01-01, 5d
    需求文档    :done, des2, after des1, 3d
    section 设计
    系统设计    :active, des3, after des2, 5d
    UI设计      :des4, after des2, 4d
    section 开发
    前端开发    :des5, after des3, 10d
    后端开发    :des6, after des3, 10d
```

## 饼图 (Pie Chart)

### 基本语法
```mermaid
pie title 数据分布
    "类别1" : 30
    "类别2" : 50
    "类别3" : 20
```

## 常用样式

### 样式定义
```mermaid
graph TD
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px
    classDef primary fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef success fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    classDef warning fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    classDef danger fill:#ffebee,stroke:#c62828,stroke-width:2px

    A:::primary
    B:::success
    C:::warning
    D:::danger
```

### 子图
```mermaid
graph TD
    subgraph Group1 [组1]
        A[A节点]
        B[B节点]
    end
    subgraph Group2 [组2]
        C[C节点]
        D[D节点]
    end
    A --> C
    B --> D
```

## 最佳实践

1. **节点命名**：使用简洁清晰的标识符
2. **布局控制**：适当使用方向和换行符控制布局
3. **样式一致**：统一样式定义，保持视觉一致
4. **注释说明**：添加title和说明文字
5. **复杂度控制**：过于复杂的图表考虑拆分
