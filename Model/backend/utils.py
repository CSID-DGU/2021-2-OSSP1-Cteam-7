from .base import BaseEmbedder
from .sentencetransformers import SentenceTransformerBackend


def select_backend(embedding_model) -> BaseEmbedder:
    """ `all-MiniLM-L6-v2` for English and `paraphrase-multilingual-MiniLM-L12-v2` for all other languages

    Returns:
        model: Either a Sentence-Transformer or Flair model
    """
    # keybert language backend
    if isinstance(embedding_model, BaseEmbedder):
        return embedding_model

    # Flair word embeddings
    if "flair" in str(type(embedding_model)):
        from flair import FlairBackend
        return FlairBackend(embedding_model)

    # Spacy embeddings
    if "spacy" in str(type(embedding_model)):
        from spacy import SpacyBackend
        return SpacyBackend(embedding_model)

    # Gensim embeddings
    if "gensim" in str(type(embedding_model)):
        from gensim import GensimBackend
        return GensimBackend(embedding_model)

    # USE embeddings
    if "tensorflow" and "saved_model" in str(type(embedding_model)):
        from use import USEBackend
        return USEBackend(embedding_model)

    # Sentence Transformer embeddings
    if "sentence_transformers" in str(type(embedding_model)):
        return SentenceTransformerBackend(embedding_model)

    # Create a Sentence Transformer model based on a string
    if isinstance(embedding_model, str):
        return SentenceTransformerBackend(embedding_model)

    return SentenceTransformerBackend("paraphrase-multilingual-MiniLM-L12-v2")
