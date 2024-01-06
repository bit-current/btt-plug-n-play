# import bittensor as bt
import os
import logging
from logging.handlers import TimedRotatingFileHandler

# function performs a deeper search past the bitcurrent directory 
def search_directory(start_directory, target_directory):
    current_directory = start_directory
    while current_directory:
        for root, dirs, files in os.walk(current_directory):
            if target_directory in dirs:
                found_directory_path = os.path.join(root, target_directory)
                # print(f"Found: {found_directory_path}")
                return found_directory_path  # Return or do something with the found directory path

        # Move to the parent directory
        parent_directory = os.path.dirname(current_directory)
        if parent_directory == current_directory:
            # If the parent is the same as the current, it means we are at the root and should break the loop
            break
        current_directory = parent_directory

    raise FileNotFoundError(f"Directory '{target_directory}' not found in or above '{start_directory}'")


