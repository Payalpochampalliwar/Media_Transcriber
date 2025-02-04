import os
import json

def save_transcription(file_path, text, output_folder="transcriptions", output_format="json"):
    """
    Saves the transcription text to a file.

    Args:
        file_path (str): Path to the original media file.
        text (str): Transcribed text.
        output_folder (str): Folder to store transcriptions.
        output_format (str): File format to save ("txt" or "json").
    """
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists
    
    base_name = os.path.basename(file_path)
    output_path = os.path.join(output_folder, f"{base_name}.{output_format}")

    if output_format == "txt":
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    elif output_format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"file": file_path, "transcription": text}, f, indent=4)

    print(f"Transcription saved at: {output_path}")
