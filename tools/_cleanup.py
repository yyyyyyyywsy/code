import os
import shutil

# Files to clean up
cleanup_files = [
    r"D:\agent_project\自动化配置\mimocode_result\tools\_copy_checkpoint.py",
    r"D:\agent_project\自动化配置\mimocode_result\tools\_read_checkpoint.py",
    r"D:\agent_project\自动化配置\mimocode_result\intermediate\checkpoint.md",
    r"D:\agent_project\自动化配置\mimocode_result\intermediate\checkpoint_backup.md",
]

print("Cleaning up temporary files...")
for file_path in cleanup_files:
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"  ✅ Removed: {file_path}")
        except Exception as e:
            print(f"  ❌ Failed to remove {file_path}: {e}")
    else:
        print(f"  ⚠️ Not found: {file_path}")

print("\nCleanup complete!")
print("Remaining files:")
for root, dirs, files in os.walk(r"D:\agent_project\自动化配置\mimocode_result"):
    for file in files:
        if not file.startswith('.'):
            print(f"  {os.path.join(root, file)}")
