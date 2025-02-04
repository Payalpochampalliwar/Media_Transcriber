import subprocess
from pathlib import Path

def extract_audio(video_path):
    """
    Extracts audio from a video file using ffmpeg.
    
    Args:
        video_path (str): Path to the video file.

    Returns:
        str: Path to the extracted audio file.
    """
    audio_path = str(Path(video_path).with_suffix('.mp3'))
    
    command = f"ffmpeg -i \"{video_path}\" -q:a 0 -map a \"{audio_path}\" -y"
    subprocess.run(command, shell=True, check=True)
    
    return audio_path
