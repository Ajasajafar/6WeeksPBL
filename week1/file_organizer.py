import os
import  shutil

fileExtensions = {
    "Docs" : ['.doc', '.docx', '.txt', '.rtf', '.pdf', '.odt', '.xlx', '.xlsx', '.ppt', '.pptx', '.csv'],
    'images' : ['.jpg', '.jpeg', '.png', 'gif', '.bmp', '.tif', '.tiff', '.psd', '.svg'],
    'Audio' : ['.mp3', '.wav', '.aac', '.wma', '.m4a'],
    'Video' : ['mp4', '.mov', '.flv', 'avi', '.wmv'],
    'system' : ['.exe', 'dll', '.bat', '.sys', '.ini', '.cfg'],
    'Archive' : ['.zip', '.rar', '.7z', '.tar'],
    'WebFile' : ['.html','.css', 'php', '.xml']
}

source_folder = input()
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isdir(file_path):
        continue
    root, ext = os.path.splitext(filename)
moved = False
for folder_name, extensions in fileExtensions.items():
    if ext.lower() in extensions:
        dest_folder = os.path.join(source_folder,folder_name)
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, filename))
        print(f"Moved: {filename} to {folder_name}")
        moved = True
        break
    if not moved:
        other_folder = os.path.join(source_folder, 'Others')
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, filename))
        print(f"Moved: {filename} to Others")