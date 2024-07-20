from litellm import embedding

from mem0.embeddings.base import EmbeddingBase


class LiteLLMEmbedding(EmbeddingBase):
    def __init__(self, model="embed-english-v3.0"):
        self.model = model
        self.dims = 1024

    def embed(self, text):
        """
        Get the embedding for the given text using LiteLLM.

        Args:
            text (str): The text to embed.

        Returns:
            list: The embedding vector.
        """
        response = embedding(model=self.model, input=[text])
        return(response['data'][0]['embedding'])

