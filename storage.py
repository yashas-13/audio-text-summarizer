"""Simple JSONL transcript storage."""
import json
from pathlib import Path
from typing import Dict, List


class TranscriptStorage:
    def __init__(self, directory: Path):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.file = self.directory / "transcripts.jsonl"

    def append(self, audio_name: str, text: str) -> None:
        record = {"audio": audio_name, "text": text}
        with self.file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def load_all(self) -> List[Dict[str, str]]:
        if not self.file.exists():
            return []
        with self.file.open("r", encoding="utf-8") as f:
            return [json.loads(line) for line in f]
