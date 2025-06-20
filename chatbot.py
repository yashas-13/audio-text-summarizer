"""Simple chatbot interface leveraging a language model."""
from typing import List

from transformers import pipeline

from vector_store import VectorStore


class ChatBot:
    def __init__(self, vector_store: VectorStore):
        # Using a small open model to keep resource usage low
        self.vector_store = vector_store
        self.generator = pipeline(
            "text-generation", model="distilgpt2", max_new_tokens=100
        )

    def answer(self, query: str) -> str:
        results = self.vector_store.search(query, k=3)
        context = "\n".join(r["text"] for r in results)
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        response = self.generator(prompt)[0]["generated_text"]
        return response[len(prompt) :].strip()
