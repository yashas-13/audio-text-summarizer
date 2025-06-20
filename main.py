"""Entry point for processing audio files and chatting with transcripts."""
from pathlib import Path

from stream_handler import get_audio_files
from transcriber import transcribe_audio
from storage import TranscriptStorage
from vector_store import VectorStore
from chatbot import ChatBot


def process_audio(audio_dir: Path, storage: TranscriptStorage, vectors: VectorStore) -> None:
    for audio_path in get_audio_files(audio_dir):
        text = transcribe_audio(audio_path)
        storage.append(audio_path.name, text)
        vectors.add(text, {"audio": audio_path.name})


def main() -> None:
    audio_dir = Path("data/audio_chunks")
    transcript_dir = Path("data/transcripts")
    storage = TranscriptStorage(transcript_dir)
    vectors = VectorStore(Path("data/faiss.index"))

    process_audio(audio_dir, storage, vectors)

    bot = ChatBot(vectors)
    while True:
        query = input("Ask about your call data (or 'exit'): ")
        if query.lower() == "exit":
            break
        answer = bot.answer(query)
        print("AI:", answer)


if __name__ == "__main__":
    main()
