import os


from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import VectorDBQA, OpenAI

import pinecone

pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment=os.environ.get("PINECONE_ENV"))

if __name__ == '__main__':
    print('Hello Vector Store')
    loader = TextLoader("/home/nesov/Programmation/LLM-LangChain/Misc/Texts/NNEmbeddingsArticle.txt")
    document = loader.load()
    print(document)

    text_splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    # take the text chunks and it will use the OpenAI embeddings API in order to converte those texts into vectors.
    # Those vectors are going to be stored in Pinecone
    docsearch = Pinecone.from_documents(texts, embeddings, index_name="medium-blog-embeddings-index")

    # https://blog.langchain.dev/retrieval/

    qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore = docsearch)

    query = "Wat are Neural Network Embeddings? Give me a 15 word anwer for a beginner"
    result = qa({"query":query})
    
    print(result)