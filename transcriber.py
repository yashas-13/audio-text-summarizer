"""Audio transcription utilities using faster-whisper."""
from pathlib import Path
from typing import List

from faster_whisper import WhisperModel

_model = None


def _load_model() -> WhisperModel:
    global _model
    if _model is None:
        # Using the small model by default; adjust as needed.
        _model = WhisperModel("small")
    return _model


def transcribe_audio(audio_path: Path) -> str:
    """Transcribe an audio file and return the text."""
    model = _load_model()
    segments, _ = model.transcribe(str(audio_path))
    text = " ".join(segment.text for segment in segments)
    return text
