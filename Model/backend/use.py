import numpy as np
from tqdm import tqdm
from typing import List

from .base import BaseEmbedder


class USEBackend(BaseEmbedder):
    def __init__(self, embedding_model):
        super().__init__()

        try:
            embedding_model(["test sentence"])
            self.embedding_model = embedding_model
        except TypeError:
            raise ValueError("Please select a correct USE model: \n")

    def embed(self,
              documents: List[str],
              verbose: bool = False) -> np.ndarray:

        embeddings = np.array([self.embedding_model([doc]).cpu().numpy()[0]
                               for doc in tqdm(documents, disable=not verbose)])
        return embeddings
