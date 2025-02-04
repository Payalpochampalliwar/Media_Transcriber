import whisper

def transcribe_audio(file_path, model_size="tiny"):
    """
    Transcribes the given audio file using OpenAI Whisper.

    Args:
        file_path (str): Path to the audio file.
        model_size (str): Whisper model size ("tiny", "base", "small", etc.).

    Returns:
        str: Transcribed text.
    """
    model = whisper.load_model(model_size)  # Load Whisper model
    result = model.transcribe(file_path)
    
    return result["text"]
