# Structuring the unstructured (article under construction)

![text_to_numeric](https://raw.githubusercontent.com/alexnesov/LLMs-and-Agents/main/Use%20Case/Diagrams%20%26%20IMGs/embedding_text.jpg)   
Image reference: OpenAI

### Adding Structure to Unstructured data

Embeddings, such as word embeddings in natural lagugage processing (NLP), are a way of **adding structure** to unstructured data. For instance, words in their raw form are unstructured data. When we use word embeddings to represent these words, we are **converting** these words into numerical vectors in a high-dimensional space, thereby adding a structure to them.

### Capturing Inherent Relationships Through Embeddings

Moreover, this structure is not arbitrary. It is designed to capture semantic or syntactic relationships between the data points. For instance, in word embeddings, words with similar meanings often have similar vectors. Hence, words are structured in such a way that the geometric relationships between the vectors capture semantic or syntactic relationships between the words.

**What is an embedding by the way?**

It is simply the transformation of text into numeric values.  

Words in their raw form are unstructured, from a computational point of view (they **are** structured from a humand standpoint, but not for a computer).

```
pip install gensim
```

Here's a Python example to create word embeddings with two dimensions:
```
from gensim.models import Word2Vec

# Sample sentences for training the word embeddings
sentences = [
    ['apple', 'fruit'],
    ['banana', 'fruit'],
    ['carrot', 'vegetable'],
    ['bike', 'vehicle'],
    ['lion', 'animal'],
    ['book', 'reading'],
    ['computer', 'technology'],
]

# Training the Word2Vec model with 2 dimensions
model = Word2Vec(sentences, vector_size=2, window=5, min_count=1, sg=1)

# Get the word vector for a specific word
word_vector = model.wv['apple']
print("Word vector for 'apple':", word_vector)

# Find similar words based on vector similarity
similar_words = model.wv.most_similar('fruit')
print("Words similar to 'fruit':", similar_words)
```

## What is a "structure" for a computer by the way?

Here, taking a philosophy of technology tangant may be interesting. It poses the question of **technological mediation** (i. e. how technology mediates our relationship with reality, everything becomes a numeric value, and by extension, a vector)
Indeed, everything starts from this question in our context.  

**What is that, fundamentally, differentiates structured from unstructured?**  

It seems that we can reply with one generic word: **structure** and **standardization** of the format.
