import os

def count_files(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return len(files)
    else:
        print(f"The folder {folder_path} does not exist or is not a directory.")
        return 0

folders = [
    r"/Users/hoangnamvu/Downloads/a/train/images",
    r"/Users/hoangnamvu/Downloads/a/train/targets",
    r"/Users/hoangnamvu/Downloads/a/test/images",
    r"/Users/hoangnamvu/Downloads/a/test/targets",
    r"/Users/hoangnamvu/Downloads/a/hold/images",
    r"/Users/hoangnamvu/Downloads/a/hold/targets"
]

for folder in folders:
    file_count = count_files(folder)
    print(f"Folder: {folder}, Number of files: {file_count}")
