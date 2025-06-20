# Call Intelligence AI - Open Source Audio-to-Chatbot Pipeline

## Overview

This project enables continuous transcription of audio (e.g. phone call recordings), storage of transcriptions, semantic search using vector embeddings, and a conversational chatbot interface for querying call history.

Entirely built with open-source tools.

## Features

* Real-time or batch audio transcription using OpenAI's Whisper (via `faster-whisper`)
* Transcript storage in JSONL format
* Semantic search with FAISS + Sentence Transformers
* Chatbot powered by open-source LLMs (e.g. Mistral via Hugging Face Transformers)
* Modular and extensible Python codebase

## Tech Stack

* Python 3.9+
* Whisper via `faster-whisper`
* `sentence-transformers` for text embeddings
* `faiss-cpu` for vector similarity search
* `transformers` for LLM chatbot
* Local file storage (can be extended to DBs)

## Folder Structure

```
call-intel-ai/
├── main.py                # Pipeline entry point
├── stream_handler.py      # Simulated audio stream
├── transcriber.py         # Whisper integration
├── storage.py             # Transcript storage logic
├── vector_store.py        # FAISS-based vector storage
├── chatbot.py             # QA interface
├── requirements.txt
├── README.md
└── data/
    ├── audio_chunks/      # Audio .wav files (input)
    └── transcripts/       # JSONL transcript logs
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/call-intel-ai.git
cd call-intel-ai
```

### 2. Set Up Python Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Prepare Audio Files

Place `.wav` files in `./data/audio_chunks/` directory.

### 4. Run the Application

```bash
python main.py
```

The script will stream the audio files, transcribe, embed, and allow you to ask questions about the calls.

## Example Chat

```
Ask about your call data: What did the customer say about delivery?
AI: The customer asked if the delivery could be rescheduled to Monday.
```

## Requirements

```txt
faster-whisper
sentence-transformers
faiss-cpu
transformers
torch
tqdm
```

## License

This project is open-source under the MIT License.

---

## Roadmap

* [ ] Live audio ingestion via Twilio/Asterisk
* [ ] Speaker diarization
* [ ] Long-context LLM support
* [ ] Web interface (Streamlit or FastAPI)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Maintainers

* \[@your-name] - lead dev
