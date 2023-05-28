import os
import shutil

def copy_files(source_dir, destination_dir):
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        if os.path.isfile(destination_file):
            # If file already exists in the destination directory, replace it
            os.remove(destination_file)

        shutil.copy2(source_file, destination_dir)
        print(f"Copied: {file_name}")


# X_Parse_Agnostic/Parse_Agnostic -> image-parse-agnostic-v3.2
source_directory = r"D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W\test\Parse_Agnostic"
destination_directory = r"D:\MP3_Django_Test_2_W\myproject\_Data\image-parse-agnostic-v3.2"
copy_files(source_directory, destination_directory)


# X_Parse_Agnostic/Human_Agnostic -> agnostic-v3.2
source_directory = r"D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W\test\Human_Agnostic"
destination_directory = r"D:\MP3_Django_Test_2_W\myproject\_Data\agnostic-v3.2"
copy_files(source_directory, destination_directory)
