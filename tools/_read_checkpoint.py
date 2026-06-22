import os

path = os.path.expanduser(r"~\.local\share\mimocode\memory\sessions\ses_13a262501ffeTRIZHGLYEROs1D\checkpoint.md")
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    print(f"File exists, size: {len(content)} bytes")
    print("---CONTENT START---")
    print(content)
    print("---CONTENT END---")
else:
    print("File does not exist")
