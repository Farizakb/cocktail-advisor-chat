import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json
import os

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


# Path to FAISS index
FAISS_INDEX_PATH = "faiss_index.bin"
COCKTAILS_JSON = "cocktail_dataset.json"

class FaissIndex:
    def __init__(self):
        self.index = None
        self.cocktail_data = []
        self.load_data()

    def load_data(self):
        """Load cocktail dataset and create FAISS index."""
        if os.path.exists(COCKTAILS_JSON):
            with open(COCKTAILS_JSON, "r", encoding="utf-8") as file:
                self.cocktail_data = json.load(file)

            embeddings = np.array([model.encode(" ".join(c["ingredients"])) for c in self.cocktail_data], dtype=np.float32)
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
            self.index.add(embeddings)

            # Save FAISS index
            faiss.write_index(self.index, FAISS_INDEX_PATH)

    def search(self, query: str, k: int = 5):
        """Search FAISS index for similar cocktails."""
        if not os.path.exists(FAISS_INDEX_PATH):
            print("FAISS index not found. Please rebuild it.")
            return []

        # Load FAISS index if not already loaded
        if self.index is None:
            self.index = faiss.read_index(FAISS_INDEX_PATH)

        query_embedding = np.array([model.encode(query)], dtype=np.float32)
        distances, indices = self.index.search(query_embedding, k)
        
        results = []
        for idx in indices[0]:
            if 0 <= idx < len(self.cocktail_data):
                results.append(self.cocktail_data[idx])
        
        return results

# Initialize FAISS index
faiss_index = FaissIndex()
