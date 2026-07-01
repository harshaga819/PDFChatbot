import os
import gc
import streamlit as st
from pdf_index import index_pdf
from chat import get_chat_chain
from config import CHROMA_PATH, DATA_DIR, UPLOADED_PDF_PATH

st.set_page_config(page_title="PDF Chatbot", layout="centered")

st.title("PDF Chatbot")
st.caption("Upload a PDF and ask questions about it. Answers come only from your document.")

# Session state

if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "indexed" not in st.session_state:
    st.session_state.indexed = False

# If a Chroma DB already exists on disk (e.g. app was restarted), load it
if not st.session_state.indexed and os.path.exists(CHROMA_PATH):
    try:
        st.session_state.chat_chain = get_chat_chain()
        st.session_state.indexed = True
    except Exception:
        pass


# Sidebar - upload & controls

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Index PDF", use_container_width=True):
            os.makedirs(DATA_DIR, exist_ok=True)
            with open(UPLOADED_PDF_PATH, "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.session_state.chat_chain = None
            gc.collect()

            with st.spinner("Indexing PDF... this may take a moment"):
                try:
                    result = index_pdf(UPLOADED_PDF_PATH)
                    st.session_state.chat_chain = get_chat_chain()
                    st.session_state.indexed = True
                    st.session_state.messages = []
                    st.success(result)
                except Exception as e:
                    st.error(f"Indexing failed: {e}")

    st.divider()

    if st.button(
        "Clear Chat",
        use_container_width=True,
        disabled=not st.session_state.indexed,
    ):
        st.session_state.messages = []
        st.rerun()

# Main chat area

if not st.session_state.indexed:
    st.info("Upload and index a PDF to start chatting.")
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_query = st.chat_input("Ask a question about your document...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = st.session_state.chat_chain.invoke(user_query)
                except Exception as e:
                    answer = f"Something went wrong while answering: {e}"
            st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})