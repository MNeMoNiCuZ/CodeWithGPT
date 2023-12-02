import sys
import os

def list_filenames(files):
    for file in files:
        # Extract the filename without extension
        filename_without_extension = os.path.splitext(os.path.basename(file))[0]
        print(filename_without_extension)

# This comment is not necessary
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        filename = os.path.basename(arg)
        print(filename.split('.')[0])
    # Pause the script to allow you to copy the filenames
    input("Press Enter to close...")