import os

main_dir = 'MyFiles'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print(f"Created directory: {main_dir}")
else:
    print(f"Directory already exists: {main_dir}")
subdirs = ['Docs', 'Images', 'Videos']

for subdir in subdirs:
    path = os.path.join(main_dir, subdir)
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Created subdirectory: {path}")
    else:
        print(f"Subdirectory already exists: {path}")
