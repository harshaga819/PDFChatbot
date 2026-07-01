import gc
import os
from langchain_chroma import Chroma
from utils import load_pdf, split_documents, load_embeddings
from config import CHROMA_PATH, COLLECTION_NAME


def _delete_existing_collection():
    """
    Clear out the previous collection so a new upload never mixes with
    stale chunks. This goes through Chroma's own delete_collection() API
    rather than deleting files on disk directly - removing the on-disk
    folder while an earlier Chroma client still holds an open SQLite
    connection fails on Windows (WinError 32: file in use).
    """
    if not os.path.exists(CHROMA_PATH):
        return

    embeddings = load_embeddings()
    try:
        vectorstore = Chroma(
            persist_directory=CHROMA_PATH,
            collection_name=COLLECTION_NAME,
            embedding_function=embeddings,
        )
        vectorstore.delete_collection()
    except Exception:
        # Nothing to delete yet, or the store is empty/corrupt - safe to
        # ignore, _store_vectors() will (re)create the collection fresh.
        pass
    finally:
        gc.collect()


def _store_vectors(chunks):
    embeddings = load_embeddings()
    return Chroma.from_documents(documents=chunks, embedding=embeddings, collection_name=COLLECTION_NAME, persist_directory=CHROMA_PATH,)


def index_pdf(pdf_path: str) -> str:
    """
    Loads, splits, and indexes a single PDF into a fresh ChromaDB store.

    Any existing vector store is deleted first, since this project is
    designed around one active document at a time rather than multi-doc
    or multi-user storage.
    """
    documents = load_pdf(pdf_path)
    chunks = split_documents(documents)

    _delete_existing_collection()
    _store_vectors(chunks)

    return f"Successfully indexed {len(chunks)} chunks."


if __name__ == "__main__":
    pdf_path = "data/uploaded.pdf"
    print(index_pdf(pdf_path))