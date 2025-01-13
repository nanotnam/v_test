import os
folders = [
    r"/Users/hoangnamvu/Downloads/train/images",
    r"/Users/hoangnamvu/Downloads/train/targets",
    r"/Users/hoangnamvu/Downloads/test/images",
    r"/Users/hoangnamvu/Downloads/test/targets",
    r"/Users/hoangnamvu/Downloads/hold/images",
    r"/Users/hoangnamvu/Downloads/hold/targets"
]

for folder in folders:
    if os.path.exists(folder) and os.path.isdir(folder):
        for file_name in os.listdir(folder):
            if "post" in file_name:  
                file_path = os.path.join(folder, file_name)
                if os.path.isfile(file_path):  
                    os.remove(file_path)

print("xoa file k can xong")

def sort_and_rename(folder_path):
    
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        files.sort() 
        
        for i, file_name in enumerate(files, start=1):
            old_path = os.path.join(folder_path, file_name)
            new_name = f"img{i}{os.path.splitext(file_name)[1]}" 
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)

for folder in folders:
    sort_and_rename(folder)

print("rename file xong")