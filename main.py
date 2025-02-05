import os
from transcriber.file_scanner import find_media_files
from transcriber.audio_extract import extract_audio
from transcriber.transcriber import transcribe_audio
from transcriber.saver import save_transcription
from transcriber.config import MODEL_SIZE

def process_directory(directory):
    """
    Processes all media files in the given directory.
    
    Args:
        directory (str): Path to the folder containing media files.
    """
    print("??? Scanning for media files...")
    media_files = find_media_files(directory)

    if not media_files:
        print("❌ No media files found. Exiting...")
        return

    for file_path in media_files:
        print(f"\n??? Processing: {os.path.basename(file_path)}")

        # Extract audio if it's a video file
        if file_path.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.webm')):
            print("??? Extracting audio from video...")
            file_path = extract_audio(file_path)

        # Transcribe the audio
        print("??? Transcribing audio...")
        text = transcribe_audio(file_path, MODEL_SIZE)

        # Save transcription
        save_transcription(file_path, text)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ").strip()
    
    if os.path.exists(folder_path):
        process_directory(folder_path)
    else:
        print("❌ Invalid directory. Please check the path and try again.")
