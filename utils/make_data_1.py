import os
import shutil

folders = [
    r"/Users/hoangnamvu/Downloads/train/images",
    r"/Users/hoangnamvu/Downloads/train/targets",
    r"/Users/hoangnamvu/Downloads/test/images",
    r"/Users/hoangnamvu/Downloads/test/targets",
    r"/Users/hoangnamvu/Downloads/hold/images",
    r"/Users/hoangnamvu/Downloads/hold/targets"
]

# File removal step
for folder in folders:
    if os.path.exists(folder) and os.path.isdir(folder):
        for file_name in os.listdir(folder):
            if "post" in file_name:  
                file_path = os.path.join(folder, file_name)
                if os.path.isfile(file_path):  
                    os.remove(file_path)

print("Deleted unnecessary files.")

# Sorting and renaming into new folders
def sort_and_copy(folder_path, new_base_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        files.sort()  # Sort files alphabetically

        # Create a new folder for the renamed files
        new_folder = os.path.join(new_base_path, os.path.basename(folder_path))
        os.makedirs(new_folder, exist_ok=True)

        # Rename and copy files to the new folder
        for i, file_name in enumerate(files, start=1):
            old_path = os.path.join(folder_path, file_name)
            new_name = f"img{i}{os.path.splitext(file_name)[1]}"  # Sequential naming
            new_path = os.path.join(new_folder, new_name)
            shutil.copy2(old_path, new_path)  # Copy the file to the new folder

        print(f"Renamed files from {folder_path} to {new_folder}.")

# Base path for the new folders
new_base_path = [
    r"/Users/hoangnamvu/Downloads/a/train",
    r"/Users/hoangnamvu/Downloads/a/train",
    r"/Users/hoangnamvu/Downloads/a/test",
    r"/Users/hoangnamvu/Downloads/a/test",
    r"/Users/hoangnamvu/Downloads/a/hold",
    r"/Users/hoangnamvu/Downloads/a/hold"
]

i = 0
# Process each folder
for folder in folders:
    sort_and_copy(folder, new_base_path[i])
    i+=1

print("Processing complete. Renamed files are stored in the new folders.")
