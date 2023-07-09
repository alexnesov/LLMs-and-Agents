# Embeddings as a pre-processing tool in the context of a legal document analysis



## Embeddings to avoid a wrong association of dates in a large text

When it comes to using embeddings for a large text, the model typically operates on smaller units of text, such as sentences or paragraphs. The embedding model doesn't explicitly split the text into chunks; instead, it processes the text sequentially or in batches, depending on the implementation.

Coming back to our heading problem you see how this will help. Headers will be isolated entities for their own meaning, while the signature date will have a totally other meaning, "**embedded**" in the context of it's phrase, where you will explicitely see the word "signature" or any other word related to a signature.

## Because embeddings unveil the meaning based on distances between sentences and words, while LLMs use a probabilistic approach

1. Probabilistic Approach of LLM: Language models like LLMs make predictions based on probabilities. They estimate the likelihood of certain sequences of words based on the patterns they've learned from training data. In the case of our document, if the LLM observed a pattern where header dates were often associated with dates in other parts of the document, it might have assigned a higher probability to the header date being the signature date. And here, we see the limitation of the LLM since we don't feed the large text at once.

2. Embeddings and Distance-based Meaning: Embeddings, such as word embeddings or contextualized embeddings, represent words or phrases as dense vectors in a high-dimensional space. These embeddings are learned to capture semantic relationships between words based on their contextual usage. In this sense, embeddings can reflect the meaning of words by their distances in the embedding space. Words or phrases with similar meanings are often closer to each other in the embedding space.



![meaning_similarity](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Vector-based%20Information%20Retrieval%20System/meaning_similarity.png)    
Image reference: https://www.youtube.com/watch?v=e2g5ya4ZFro&ab_channel=Pinecone (Supercharging Semantic Search with Pinecone and Cohere
)