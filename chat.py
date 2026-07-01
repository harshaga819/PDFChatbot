from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

from utils import load_embeddings, load_llm, format_docs
from config import CHROMA_PATH, COLLECTION_NAME, TOP_K

PROMPT_TEMPLATE = """
You are an intelligent AI assistant.

Answer ONLY using the provided context.

Rules:

1. Answer only from the provided context.

2. If the answer is unavailable, reply exactly:

"I couldn't find that information in the provided document."

3. Never make up information.

4. Keep your answers concise, clear and well structured.

Context:
{context}

Question:
{query}

Answer:
"""


def get_chat_chain():
    """
    Builds and returns an LCEL chat chain backed by the persisted ChromaDB
    vector store. Call this after index_pdf() has run at least once.
    """
    embeddings = load_embeddings()

    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K},
    )

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    llm = load_llm()

    context_chain = retriever | RunnableLambda(format_docs)

    input_chain = RunnableParallel({
        "context": context_chain,
        "query": RunnablePassthrough(),
    })

    return input_chain | prompt | llm | StrOutputParser()