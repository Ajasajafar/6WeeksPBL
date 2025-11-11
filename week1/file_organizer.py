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
    _, ext = os.path.splitext(filename)
