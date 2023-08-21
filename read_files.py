import os
import glob
from pathlib import Path

HOME = str(Path.home())
PATH_OF_BRAIN_IMAGES = HOME + "/Downloads/for_ryan/"
PATH_TO_SAVE_FILE_PATHS = HOME + "/Downloads/input.txt"

file_paths = glob.glob(PATH_OF_BRAIN_IMAGES + "/**/*.nii.gz", recursive=True)

# print(file_paths)

# make input.txt if it does not exist
if not os.path.exists(PATH_TO_SAVE_FILE_PATHS):
    os.mknod(PATH_TO_SAVE_FILE_PATHS)

with open(PATH_TO_SAVE_FILE_PATHS, "w") as text_file:
    for file_path in file_paths:
        # text_file.write(os.path.basename(file_path) + "\n")
        text_file.write(file_path + "\n")
