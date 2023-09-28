"""
Creating and Analyzing Word Embeddings from Unstructured Data with Gensim and NLTK
"""


from gensim.models import Word2Vec
import nltk

# Let's create some mock unstructured data
data = """In the world of finance, risk management is the process of identification, analysis, and acceptance or mitigation of uncertainty in investment decisions. \
Risk management occurs anytime an investor or fund manager analyzes and attempts to quantify the potential for losses in an investment, \
such as a moral hazard, and then takes the appropriate action (or inaction) given the fund's investment objectives and risk tolerance."""

# Tokenize the data
sentences = nltk.sent_tokenize(data)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

# Train a Word2Vec model
model = Word2Vec(sentences, min_count=1)

# Find vector representation for a word, say "risk"
print(model.wv['risk'])


# Find similar words to "risk"
similar = model.wv.most_similar('risk', topn=2)
print(similar)
