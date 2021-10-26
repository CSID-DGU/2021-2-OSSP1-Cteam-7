import numpy as np
from tqdm import tqdm
from typing import List
from .base import BaseEmbedder
from gensim.models.keyedvectors import Word2VecKeyedVectors


class GensimBackend(BaseEmbedder):
    def __init__(self, embedding_model: Word2VecKeyedVectors):
        super().__init__()

        if isinstance(embedding_model, Word2VecKeyedVectors):
            self.embedding_model = embedding_model
        else:
            raise ValueError("Please select a correct Gensim model: \n")

    def embed(self,
              documents: List[str],
              verbose: bool = False) -> np.ndarray:
        vector_shape = self.embedding_model.word_vec(list(self.embedding_model.vocab.keys())[0]).shape
        empty_vector = np.zeros(vector_shape[0])

        embeddings = []
        for doc in tqdm(documents, disable=not verbose, position=0, leave=True):
            doc_embedding = []

            # Extract word embeddings
            for word in doc.split(" "):
                try:
                    word_embedding = self.embedding_model.word_vec(word)
                    doc_embedding.append(word_embedding)
                except KeyError:
                    doc_embedding.append(empty_vector)

            # Pool word embeddings
            doc_embedding = np.mean(doc_embedding, axis=0)
            embeddings.append(doc_embedding)

        embeddings = np.array(embeddings)
        return embeddings
