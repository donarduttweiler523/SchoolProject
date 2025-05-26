import os
import shutil

def move_files(src_dir, dst_dir):
    # Move all files and subdirectories from src_dir to dst_dir
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir, os.path.relpath(src_file, src_dir))
            shutil.move(src_file, dst_file)

# Set the source and destination directories
source_directory = 'src'  # Replace with the actual source directory path
destination_directory = 'dst'  # Replace with the actual destination directory path

move_files(source_directory, destination_directory)
