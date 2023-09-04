#!/usr/bin/python3

from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment=os.environ.get("PINECONE_ENV"))

if __name__ == '__main__':
    # !!! The software transfer agreement document is not private, it is a publicaly available document published by the SEC !!
    pdf_path = "Texts/Software Transfer Agreement.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index/faiss_index_react")

    new_vectorstore = FAISS.load_local("faiss_index/faiss_index_react", embeddings)
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(), chain_type="stuff", retriever=new_vectorstore.as_retriever()
    )
    res = qa.run("What is Autodesk's legal form? Response should be strictly this format: legal form")
    print(res)
    res = qa.run("When was the contract signed? Response should be strictly this (python format): dd-mm-yyyy")
    print(res)
