"""Vector storage backed by FAISS."""
import json
from pathlib import Path
from typing import List, Dict

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self, index_path: Path):
        self.index_path = Path(index_path)
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.metadata_path = self.index_path.with_suffix(".json")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dim = self.model.get_sentence_embedding_dimension()
        if self.index_path.exists():
            self.index = faiss.read_index(str(self.index_path))
            with self.metadata_path.open("r", encoding="utf-8") as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dim)
            self.metadata = []

    def add(self, text: str, metadata: Dict[str, str]):
        embedding = self.model.encode([text])[0].astype("float32")
        self.index.add(np.array([embedding]))
        self.metadata.append({"text": text, **metadata})
        faiss.write_index(self.index, str(self.index_path))
        with self.metadata_path.open("w", encoding="utf-8") as f:
            json.dump(self.metadata, f)

    def search(self, query: str, k: int = 3) -> List[Dict[str, str]]:
        if len(self.metadata) == 0:
            return []
        embedding = self.model.encode([query])[0].astype("float32")
        D, I = self.index.search(np.array([embedding]), k)
        return [self.metadata[i] for i in I[0] if i < len(self.metadata)]
