# Embeddings as a pre-processing tool to an LLM process (legal document analysis) (article under construction!)



## What did we want initially?

We wanted to extract some information from the following legal document: [Software Transfer Agreement](https://github.com/alexnesov/LLMs-and-Agents/blob/main/Use%20Case/Texts/Software%20Transfer%20Agreement.pdf)  
This document is publically available on the SEC website.

We encountered some issues with the signature Date extraction. We are going to focus precisely on this issue as it is general enough to be understood across all domains and could arise for every industry, for many use cases.   
From a technical point of view, it is not trivial at all, as we will show how it tackles the following fundamental points:

- Proximity
- Semantic Integrity
- Reconciliation

Above all, the solution to this problem (using Embeddings and a Vector Database) uses a game changing approach to extract information through LLMs.

## The LLM does exactly what you tell it to do, not what you want it to do

**Here is the issue:** 

- There was a date on each page in the header. This date is not the signature date; it is the date at which the document was downloaded
- Of course, we don't know *a priori* on which page we'll find the signature date
- The document is too large (large *context*) to be ingested as it is by the LLM, at once
- We started with a *naive* approach (simply *chunking* the text, i.e *splitting* it) to see how the LLM would handle our case
- **Issue:** the LLM "thought" that the signature date was the date in the header, for the pages where the signature date was not explicitely stated, as a whole sentence (for example: "*this document was signed on the...*")

Some would argue that we are confronted to a limitation of ChatGPT. While this view may be true without further engineering (that goes beyond some "naive" approaches), it becomes false if we pay attention to the way we ask things to the computer.

**Here is what the LLM sees when we provide the raw chunks as an input (it corresponds to the header)**

This is what the computer sees @ the raw format:  
"*5/12/23, 5:36 PM Software Transfer Agr eement*" 

Without any context, a human also would be puzzled, especially if forced him to provide an answer (*i. e.* a signature date) and that no other date was present (not even an arbitrage can be made). We can't really blame the LLM.

Here is the set of reponses we've got for every chunk (we also asked for the legal name and form):

![signature_date](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Use%20Case/Diagrams%20%26%20IMGs/sig_date.png)   

Actually, the LLMs **arbitrage**, so to speak, is not bad at all, because it got the right date when several dates were present in the same chunk, and of course, it couldn't provide the right date when there was no actual signature date present in the chunk.


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


## How does the Embedding process work in the context of an LLM app?

### Embedding, Indexing & Similarity Search parts serve to find the relevant text chunks to send to the LLM, instead of sending whole chunks like we did before


![context_injection](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Use%20Case/Diagrams%20%26%20IMGs/context_injection.jpg)  
Image reference: https://towardsdatascience.com/all-you-need-to-know-to-build-your-first-llm-app-eb982c78ffac

Check the reference of the image above to get a detailled view of how an LLM app works.

## Our personnal take: the future of AI in the context of legal-tech projects


The fact that AI could at least **assist** the lawyer is unquestionnable, at least to **review** or **reconcile** with what he or she already wrote. 
Now, the question that remains is:  

**What is the work share that will still be alocated to the lawyer?**  
There are, at least, three answers that we can provide right now:
1. There is no definitive threshold, it's dynamic, and it will certainly evolve towards more and more automation.
2. This trend towards more automation will be due to:
    - More sophisticated tools (typically, replacing a "naive" chunking approach to vectorized operations as we showed above)
    - Without even mentioning the intermediary layer that we set up ourselves, the LLM itself will be optimized (more training data, more parameters,...)
    - On an individual level: "**AI aware"**" (i. e. lawyers who are already used to AI-tech tools) will be more careful in the way they write and format documents, which will lead to a legal superstructure that will be more prone to automation
3. On a sociologic level: the legal landscape generally will evolve to higher productivity levels, imposing social norms or even standards to avoid hallucinations



## When NOT to use FAISS: specific companies linked to a national context

From our experience, FAISS works better for general clustering when the proximity between a spcific enterprise for example to a certain country doesn't matter.
Very concreteyle speaking, from our Use Case, ChatGPT is going to perform very well at linking SES Satelittes (a leading Satelitte company in Luxemourg) with Luxembourg for example. For ChatGPT, this "makes sense", while it doesn't for FAISS, because FAISS operates in a more abstract level, so to speak. This is very probably due to the superior amount of training data used during GPT's training sessions.