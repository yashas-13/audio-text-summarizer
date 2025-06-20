from pathlib import Path
from typing import Iterator


def get_audio_files(directory: Path) -> Iterator[Path]:
    """Yield audio files from a directory sorted by name."""
    directory = Path(directory)
    if not directory.exists():
        return
    for path in sorted(directory.glob("*.wav")):
        yield path
