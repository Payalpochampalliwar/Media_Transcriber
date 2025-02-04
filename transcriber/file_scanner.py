import os 
from pathlib import Path

def find_media_files(directory):
    """
    Recursively scans the given directory for media files (audio and video).
    
    Args:
        directory (str): Path to the folder to scan.

    Returns:
        list: List of media file paths.
    """
    media_extensions = {'.mp3', '.mp4', '.avi', '.mov'}
    media_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix in media_extensions:
                media_files.append(os.path.join(root, file))

    return media_files