import os
import shutil

def cleanup_temp_files(temp_dirs):
    for directory in temp_dirs.values():
        if os.path.exists(directory):
            shutil.rmtree(directory)
            os.makedirs(directory, exist_ok=True)
