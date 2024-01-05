# import bittensor as bt
import os


def search_directory(start_directory, target_directory):
    for root, dirs, files in os.walk(start_directory):
        if target_directory in dirs:
            # Full path to the found directory
            found_directory_path = os.path.join(root, target_directory)
            return found_directory_path
    raise FileNotFoundError(f"Directory '{target_directory}' not found in '{start_directory}' and its subdirectories")
