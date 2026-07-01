import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from config import EMBEDDING_MODEL, LLM_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

load_dotenv()


def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load()


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)


def load_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def load_llm():
    return ChatGoogleGenerativeAI(model=LLM_MODEL, temperature=0.3, google_api_key=os.getenv("GOOGLE_API_KEY"))


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)