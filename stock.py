
import os
import streamlit as st
import pickle
import time
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Streamlit app
st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Collect URLs from user input
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}", "")
    if url.strip():
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(
    temperature=0.9,
    max_tokens=500,
    openai_api_key=os.getenv("OPENAI_API_KEY", "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")
)

if process_url_clicked:
    if not urls:
        st.sidebar.error("Please enter at least one valid URL.")
    else:
        try:
            # Load and process data from URLs
            loader = UnstructuredURLLoader(urls=urls)
            main_placeholder.text("Loading data... ✅")
            data = loader.load()

            # Split data into smaller documents
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            main_placeholder.text("Splitting text... ✅")
            docs = text_splitter.split_documents(data)

            # Create embeddings and build FAISS index
            embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY", "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"))
            vectorstore_openai = FAISS.from_documents(docs, embeddings)
            pkl = vectorstore_openai.serialize_to_bytes()
            main_placeholder.text("Building embedding vectors... ✅")
            time.sleep(2)

            # Save FAISS index to pickle file
            with open(file_path, "wb") as f:
                pickle.dump(pkl, f)
            main_placeholder.success("Processing completed!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Input field for user query
query = main_placeholder.text_input("Question: ")

if query:
    try:
        if os.path.exists(file_path):
            # Load and deserialize FAISS index
            with open(file_path, "rb") as f:
                pkl = pickle.load(f)
            vectorstore = FAISS.deserialize_from_bytes(
                embeddings=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY", "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")),
                serialized=pkl,
                allow_dangerous_deserialization=True
            )
            
            # Create a retrieval question-answering chain
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)

            # Display results
            st.header("Answer")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                for source in sources.split("\n"):
                    st.write(source)
        else:
            st.error("No processed data found. Please process URLs first.")
    except Exception as e:
        st.error(f"An error occurred while processing your query: {e}")
