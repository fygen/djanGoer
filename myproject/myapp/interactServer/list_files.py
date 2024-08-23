from pathlib import Path
import os

# Specify the directory path
print(os.getcwd())
# directory = Path(os.getcwd()+'/media/')
print(os.listdir(path=Path.join(os.getcwd(),'/media/')))

# Get a list of all files in the directory
files = [file for file in directory.iterdir() if file.is_file()]

# Print the list of files
print(files)
