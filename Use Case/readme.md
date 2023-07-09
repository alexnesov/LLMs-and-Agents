# Embeddings as a pre-processing tool in the context of a legal document analysis


## What did we want to do initially?

We wanted to extract some information from the following legal document: [Software Transfer Agreement](https://github.com/alexnesov/LLMs-and-Agents/blob/main/Use%20Case/Texts/Software%20Transfer%20Agreement.pdf)  
This document is publically available on the SEC website.

We encountered some issues with the signature Date extraction. We are going to focus precisely on this issue as it is general enough to be understood across all domains and could arise in every industry. And from a technical point of view, it is not trivial at all.
Above all, the solution to this problem (using Embeddings and a Vector Database) is a total breakthrough in the way one can approach information extraction.

Here is the issue: 

- There was a date on each page in the header. This date is not the signature date; it is the date at which the document was downloaded.
- Of course, we don't know a priori on which page we'll find the signature date.
- The document is too large (large *context*) to be ingested as it is by the LLM
- We started with a *naive* approach to see how the LLM would handle our case

When dealing with a large text like this one, a common initial reflex might be to chunk it into smaller parts and process it iteratively. However, this approach is inefficient and, more importantly, it breaks the **semantic integrity** of the whole text, which can lead to mistakes (which it did).


![naive_approach](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Use%20Case/Diagrams%20%26%20IMGs/chunk.png)    


A better approach is to use embeddings for handling large texts.

## Embeddings to avoid a wrong association of dates in a large text

[Embeddings & Vector Store tutorial](https://towardsdatascience.com/all-you-need-to-know-to-build-your-first-llm-app-eb982c78ffac)


When it comes to using embeddings for a large text, the model typically operates on smaller units of text, such as sentences or paragraphs. The embedding model doesn't explicitly split the text into chunks; instead, it processes the text sequentially or in batches, depending on the implementation.

Coming back to our heading problem you see how this will help. Headers will be isolated entities for their own meaning, while the signature date will have a totally other meaning, "**embedded**" in the context of it's phrase, where you will explicitely see the word "signature" or any other word related to a signature.

## Because embeddings unveil the meaning based on distances between sentences and words, while LLMs use a probabilistic approach

1. Probabilistic Approach of LLM: Language models like LLMs make predictions based on probabilities. They estimate the likelihood of certain sequences of words based on the patterns they've learned from training data. In the case of our document, if the LLM observed a pattern where header dates were often associated with dates in other parts of the document, it might have assigned a higher probability to the header date being the signature date. And here, we see the limitation of the LLM since we don't feed the large text at once.

2. Embeddings and Distance-based Meaning: Embeddings, such as word embeddings or contextualized embeddings, represent words or phrases as dense vectors in a high-dimensional space. These embeddings are learned to capture semantic relationships between words based on their contextual usage. In this sense, embeddings can reflect the meaning of words by their distances in the embedding space. Words or phrases with similar meanings are often closer to each other in the embedding space.



![meaning_similarity](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Vector-based%20Information%20Retrieval%20System/meaning_similarity.png)    
Image reference: https://www.youtube.com/watch?v=e2g5ya4ZFro&ab_channel=Pinecone (Supercharging Semantic Search with Pinecone and Cohere
)

