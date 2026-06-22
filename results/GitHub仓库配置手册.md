# GitHub 仓库配置手册

## 1. 仓库信息

### ai_news（日报网站）
- **仓库地址**: https://github.com/yyyyyyyywsy/ai_news
- **网站地址**: https://yyyyyyyywsy.github.io/ai_news/
- **分支**: main
- **本地路径**: D:\agent_project\自动化配置\ai_news

### code（代码仓库）
- **仓库地址**: https://github.com/yyyyyyyywsy/code
- **分支**: master
- **本地路径**: D:\agent_project\自动化配置\mimocode_result

---

## 2. 目录结构

### ai_news 仓库
```
ai_news/
├─ index.html          ← 首页（卡片式新闻展示）
├─ archive.html        ← 历史归档页
├─ style.css           ← 样式
└─ daily/
    └─ 2026-06-14-full.md  ← 今日日报原文
```

### code 仓库
```
mimocode_result/
├─ README.md           ← 仓库说明
├─ python/             ← Python 代码
├─ javascript/         ← JavaScript/Node.js 代码
├─ tools/              ← 实用工具
├─ automation/         ← 自动化脚本
└─ archive/            ← 归档代码
```

---

## 3. 操作流程

### 3.1 日报网站（ai_news）

**手动更新步骤：**

```bash
# 1. 进入项目目录
cd D:\agent_project\自动化配置\ai_news

# 2. 在 MiMoCode 中执行：搜索今天的AI新闻，生成日报
#    AI 会自动抓取新闻、生成 markdown 和 HTML

# 3. 日报保存位置
D:\agent_project\自动化配置\ai_news\daily\YYYY-MM-DD-full.md

# 4. 提交推送
git add -A
git commit -m "feat: AI热点日报 - YYYY年M月D日"
git push origin main
```

### 3.2 代码仓库（code）

**手动上传步骤：**

```bash
# 1. 进入项目目录
cd D:\agent_project\自动化配置\mimocode_result

# 2. 复制文件到对应目录
#    Python → python/
#    JS/TS → javascript/
#    Shell → automation/
#    其他 → tools/

# 3. 提交推送
git add <文件路径>
git commit -m "add: <文件描述>"
git push origin master
```

**文件分类规则：**

| 扩展名 | 目标目录 |
|--------|----------|
| .py | python/ |
| .js, .ts | javascript/ |
| .sh, .ps1 | automation/ |
| 其他 | tools/ |

---

## 4. 配置信息

### 4.1 Git 配置
```bash
git config --global user.name "yyyyyyyywsy"
git config --global user.email "your-email@example.com"
```

### 4.2 GitHub CLI 认证
```bash
# 登录
gh auth login
# 选择：GitHub.com → HTTPS → Paste token
# 权限：repo, read:org, workflow

# 生成 Token
# https://github.com/settings/tokens/new
```

### 4.3 GitHub Pages 启用
```bash
gh api -X POST repos/yyyyyyyywsy/ai_news/pages \
  -f build_type=legacy \
  --input - <<EOF
{
  "source": {
    "branch": "main",
    "path": "/"
  }
}
EOF
```

---

## 5. 常见问题

### Q1: git push 认证失败
```bash
gh auth login
git config credential.helper manager
```

### Q2: GitHub Pages 部署失败
```bash
gh api repos/yyyyyyyywsy/ai_news/pages  # 检查状态
gh api -X POST repos/yyyyyyyywsy/ai_news/pages/deployments  # 重新部署
```

### Q3: 分支不一致
```bash
git branch -a
git branch -m master main
git push -u origin main
```

---

## 6. AI 代码总结功能

当上传代码到 `yyyyyyyywsy/code` 仓库时，AI 应自动为每个代码文件生成总结文档。

### 6.1 总结格式

每个代码文件上传后，应在同目录生成 `<文件名>_SUMMARY.md`：

```markdown
# <文件名> 代码总结

## 功能概述
[一句话说明代码做什么]

## 核心逻辑
[描述主要算法、流程、数据结构]

## 关键函数/类
| 名称 | 功能 | 参数 | 返回值 |
|------|------|------|--------|
| func1 | 描述 | arg1: 类型 | 返回类型 |

## 依赖
- [库名]: 用途

## 使用方式
[如何运行、调用示例]
```

### 6.2 AI 执行指令

上传代码时，AI 需执行以下步骤：

```bash
# 1. 读取代码文件
# 2. 分析代码结构、功能、依赖
# 3. 生成总结文档
# 4. 将总结文档保存到 _SUMMARY.md
# 5. 一起提交到仓库
```

### 6.3 示例

上传 `mimocode_result/python/data_parser.py` 后：
```
python/
├─ data_parser.py
├─ data_parser_SUMMARY.md
├─ utils.py
└─ utils_SUMMARY.md
```

---

## 7. 环境信息

- **系统**: Windows
- **AI 工具**: MiMoCode
- **工作目录**: D:\agent_project\自动化配置\
- **最后更新**: 2026-06-14