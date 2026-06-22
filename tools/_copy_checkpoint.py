import shutil
import os

src = os.path.expanduser(r"~\.local\share\mimocode\memory\sessions\ses_13a262501ffeTRIZHGLYEROs1D\checkpoint.md")
dst = os.path.expanduser(r"~\.local\share\mimocode\memory\sessions\ses_13a262501ffeTRIZHGLYEROs1D\checkpoint.md")

# First, let's copy the backup to the checkpoint location
backup = r"D:\agent_project\自动化配置\mimocode_result\intermediate\checkpoint.md"

if os.path.exists(backup):
    with open(backup, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add the required first line
    new_content = "Topic: AGENTS.md误删恢复 + 文件管理 + 网页优化\n\n" + content
    
    # Add the missing sub-sections
    # Find the last section (§11) and add after it
    lines = new_content.split('\n')
    new_lines = []
    
    for line in lines:
        new_lines.append(line)
        if line.strip() == "## §11 Open notes":
            new_lines.append("")
            new_lines.append("### Execution context")
            new_lines.append("(none)")
            new_lines.append("")
            new_lines.append("### Live resources")
            new_lines.append("- ai_news 仓库: https://github.com/yyyyyyyywsy/ai_news (main 分支)")
            new_lines.append("- code 仓库: https://github.com/yyyyyyyywsy/code (master 分支)")
            new_lines.append("- GitHub Pages: https://yyyyyyyywsy.github.io/ai_news/")
            new_lines.append("- 本地路径: D:\\agent_project\\自动化配置\\")
            new_lines.append("")
            new_lines.append("### Session metadata")
            new_lines.append("- Session ID: ses_13a262501ffeTRIZHGLYEROs1D")
            new_lines.append("- Start time: 2026-06-14")
            new_lines.append("- Model: mimo-auto")
            new_lines.append("")
            new_lines.append("### Discovered")
            new_lines.append("- AGENTS.md 原始内容包含：中文规则、Karpathy 四原则、Swarm 架构、产出规则、系统自带规则")
            new_lines.append("- AGENTS.md 被误删后无法恢复，需要用户提供备份")
            new_lines.append("- 每次对话开始必须先读 AGENTS.md")
            new_lines.append("")
            new_lines.append("### Dead ends")
            new_lines.append("(none)")
    
    final_content = '\n'.join(new_lines)
    
    with open(src, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Checkpoint file updated successfully: {len(final_content)} bytes")
    print("Added: Topic line, Execution context, Live resources, Session metadata, Discovered, Dead ends")
else:
    print(f"Backup file not found: {backup}")
