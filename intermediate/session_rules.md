# Session Rules - 重要规则记录

## 每次对话必须遵守

1. **先读AGENTS.md** — 每次对话开始时，必须先读 `C:\Users\王思源\.mimocode\AGENTS.md`，按文档规则执行任务
2. **输出目录** — 所有产出文件必须放到 `mimocode_result` 目录下
3. **不删evidence** — 不要删除 `.swarm/evidence/` 目录下的文件
4. **迭代上限** — `max_iterations: 5` 是全局迭代上限

## AGENTS.md 核心内容

- 语言：始终用中文回复，技术术语保持英文
- 仓库结构：配置目录，不含源代码
- Swarm架构：多智能体协作系统（architect、explorer、coder、reviewer等）
- Karpathy四原则：Think before coding、Simplicity first、Surgical changes、Goal-driven execution

## 错误记录

- 之前多次搞混目录名：opencode_result → 应为 mimocode_result
- 原因：没有先读AGENTS.md就执行任务
