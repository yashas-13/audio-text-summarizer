# Audio Text Summarizer

## Overview

This project provides an end to end pipeline for turning audio recordings into searchable text and querying them through a simple chatbot interface.  It uses open source tools such as Whisper for transcription, Sentence Transformers and FAISS for semantic search, and Hugging Face Transformers for the chatbot.

## Features

* Real-time or batch audio transcription using `faster-whisper`
* Transcript storage in JSONL format
* Semantic search with FAISS and Sentence Transformers
* Chatbot powered by an open language model (`distilgpt2` by default)
* Modular Python codebase that can be extended

## Tech Stack

* Python 3.9+
* `faster-whisper` for speech to text
* `sentence-transformers` for embeddings
* `faiss-cpu` for vector similarity search
* `transformers` for the chatbot model

## Folder Structure

```
audio-text-summarizer/
├── main.py                # Pipeline entry point
├── stream_handler.py      # Audio file iterator
├── transcriber.py         # Whisper integration
├── storage.py             # Transcript storage logic
├── vector_store.py        # FAISS-based vector storage
├── chatbot.py             # Simple QA interface
├── requirements.txt       # Python dependencies
├── README.md
└── data/
    ├── audio_chunks/      # Place .wav files here
    └── transcripts/       # JSONL transcript logs
```

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-org/audio-text-summarizer.git
   cd audio-text-summarizer
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Add audio files**

   Place your `.wav` recordings in `./data/audio_chunks/`.

4. **Run the application**

   ```bash
   python main.py
   ```

   The script transcribes the audio files, stores the transcripts, creates vector embeddings and lets you ask questions about the conversations.

## Example Usage

```
Ask about your call data (or 'exit'): What was mentioned about delivery?
AI: The customer asked if the delivery could be rescheduled to Monday.
```

## Requirements

The Python dependencies are listed in `requirements.txt` and include:

```
faster-whisper
sentence-transformers
faiss-cpu
transformers
torch
tqdm
```

## License

This project is open-source under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
