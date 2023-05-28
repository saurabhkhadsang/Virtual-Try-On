import os
import shutil

def copy_folder_files(source, destination):
    # Iterate over all items in the source directory
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            # If the item is a directory, recursively copy its contents
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        else:
            # If the item is a file, copy it to the destination directory
            shutil.copy2(source_path, destination_path)
        
        print(f"Copied: _Data -> HR-VITON/data/test")





# Copy Input
source_directory = r'D:\MP3_Django_Test_2_W\myproject\_INPUT'
destination_directory = r'D:\MP3_Django_Test_2_W\myproject\myapp\static\image\INPUT'
copy_folder_files(source_directory, destination_directory)

# Copy Output
source_directory = r'D:\MP3_Django_Test_2_W\myproject\_OUTPUT'
destination_directory = r'D:\MP3_Django_Test_2_W\myproject\myapp\static\image\OUTPUT'
copy_folder_files(source_directory, destination_directory)



