import shutil
import os

# Source file
src = r"D:\agent_project\自动化配置\mimocode_result\intermediate\checkpoint_final.md"

# Target file
dst = os.path.expanduser(r"~\.local\share\mimocode\memory\sessions\ses_13a262501ffeTRIZHGLYEROs1D\checkpoint.md")

if os.path.exists(src):
    # Copy the file
    shutil.copy2(src, dst)
    print(f"✅ Checkpoint file copied successfully!")
    print(f"   Source: {src}")
    print(f"   Target: {dst}")
    
    # Verify the copy
    if os.path.exists(dst):
        src_size = os.path.getsize(src)
        dst_size = os.path.getsize(dst)
        print(f"   Source size: {src_size} bytes")
        print(f"   Target size: {dst_size} bytes")
        if src_size == dst_size:
            print("   ✅ Verification passed: files match")
        else:
            print("   ⚠️ Warning: file sizes don't match")
    else:
        print("   ❌ Error: target file not created")
else:
    print(f"❌ Source file not found: {src}")
    print("Please run the checkpoint writer first to create the final checkpoint file.")
