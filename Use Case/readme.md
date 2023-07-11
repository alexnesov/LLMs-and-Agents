# Embeddings as a pre-processing tool to enhance information extraction accuracy in the context of a legal document analysis



     
## What did we want initially?

We wanted to extract some information from the following legal document: [Software Transfer Agreement](https://github.com/alexnesov/LLMs-and-Agents/blob/main/Use%20Case/Texts/Software%20Transfer%20Agreement.pdf)  
This document is publically available on the SEC website.

We encountered some issues with the signature Date extraction. We are going to focus precisely on this issue as it is general enough to be understood across all domains and could arise in every industry. And from a technical point of view, it is not trivial at all.
Above all, the solution to this problem (using Embeddings and a Vector Database) is a total breakthrough in the way one can approach information extraction.

## The computer does exactly what you tell it to do, not what you want it to do

Some would argue that we are confronted to a limitation of ChatGPT. While this view may be true without further engineering (that goes beyond some "naive" approaches), it becomes false if we pay attention to the way we ask things to the computer.

**Here is the issue:** 

- There was a date on each page in the header. This date is not the signature date; it is the date at which the document was downloaded.
- Of course, we don't know a priori on which page we'll find the signature date.
- The document is too large (large *context*) to be ingested as it is by the LLM, at once
- We started with a *naive* approach (simply *chunking* the text, i.e *splitting* it) to see how the LLM would handle our case
- **Issue:** the LLM "thought" that the signature date was the date in the header, for the pages where the signature date was not explicitely stated, as a whole sentence (for example: "*this document was signed on the...*")

**Here is what the LLM sees**

This is what the computer sees @ the raw format:   "*5/12/23, 5:36 PM Software Transfer Agr eement*"
Actually, the LLMs **statistical arbitrage**, so to speak, is quite good, because it got the right date when several dates were present in the same chunk:



Indeed, without further context, if we tell to a human to extract the signature date (i.e. implying that there **IS** a signature date) and if this is the only date, there are chances that some would pick this one.

We can't blame the LLM

## Rule N°1: Semantic Integrity is Queen

When dealing with a large text like this one, a common initial reflex might be to chunk it into smaller parts and process it iteratively. However, this approach is inefficient and, more importantly, it breaks the **semantic integrity** of the whole text, which can lead to mistakes (which it did).

Here is the header, present on every page:    
![Date](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Use%20Case/Diagrams%20%26%20IMGs/date.png)


Here is a simplified diagram illustring the "naive" approach:
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



Does FAISS reduce dimension? --> context 
Compression and noise reduction