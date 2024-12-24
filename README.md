# stock-analyzer
 we get required information by giving urls



 Here's your detailed `README.md` file, explaining the tools and workflow:

```markdown
# News Research Tool 📈

This project is a Streamlit-based web application that processes news articles from URLs and enables AI-powered question-answering with source references. The tool utilizes several state-of-the-art libraries and APIs to analyze and query content efficiently.

---

## Features
- Accepts up to 3 news article URLs for processing.
- Extracts and splits content into smaller chunks for analysis.
- Generates semantic embeddings using OpenAI’s API.
- Builds a FAISS vector database for fast and accurate retrieval.
- Allows users to query the processed content and receive answers with sources.

---

## Tools Used

### 1. **Streamlit**
- **Purpose**: Creates an interactive user interface for input, processing, and output.
- **Usage**:
  - Sidebar for URL input and processing button.
  - Text input box for user queries.
  - Displays answers and their sources in a user-friendly format.

---

### 2. **LangChain**
- **Purpose**: Simplifies integration with language models and provides utilities for document loading, splitting, embedding, and retrieval.
- **Usage**:
  - **UnstructuredURLLoader**: Reads content from the provided news URLs.
  - **RecursiveCharacterTextSplitter**: Splits large content into smaller, manageable chunks.
  - **RetrievalQAWithSourcesChain**: Powers the query-answering system with source references.

---

### 3. **OpenAI API**
- **Purpose**: Provides powerful language models for generating embeddings and answering queries.
- **Usage**:
  - **Embeddings**: Converts text chunks into dense vector representations for similarity search.
  - **LLM (Language Model)**: Processes user questions and generates human-like answers.

---

### 4. **FAISS (Facebook AI Similarity Search)**
- **Purpose**: Handles similarity search and clustering of vectorized text data.
- **Usage**:
  - Stores text embeddings in a vector database.
  - Quickly retrieves relevant text chunks during query processing.

---

### 5. **dotenv**
- **Purpose**: Manages environment variables securely.
- **Usage**:
  - Loads the OpenAI API key from a `.env` file to keep sensitive data secure.

---

### 6. **Pickle**
- **Purpose**: Serializes and deserializes Python objects for saving and reusing processed data.
- **Usage**:
  - Saves the FAISS vector database to a file (`faiss_store_openai.pkl`).
  - Reloads the database for query processing, avoiding redundant computations.

---

## Workflow
1. **Input**: Users enter up to 3 URLs in the sidebar.
2. **Processing**:
   - Extracts content from the URLs.
   - Splits the content into smaller chunks.
   - Generates embeddings for each chunk using OpenAI’s API.
   - Stores the embeddings in a FAISS vector database.
3. **Querying**:
   - Users type questions into the query box.
   - The tool retrieves relevant content chunks from the FAISS database.
   - OpenAI generates an answer with references to the original sources.

---

## How to Use

### Prerequisites
- Python 3.8 or above
- An OpenAI API key

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/news-research-tool.git
   cd news-research-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

### Running the App
1. Start the Streamlit app:
   ```bash
   streamlit run stock.py
   ```

2. Enter URLs in the sidebar and click "Process URLs."

3. Type your question into the text input box, and the app will display the answer with sources.

---

## Notes
- Ensure URLs contain accessible, text-rich content.
- Processed data is saved to `faiss_store_openai.pkl` to avoid reprocessing.

---

## Acknowledgements
- [Streamlit](https://streamlit.io/) for the web application framework.
- [LangChain](https://python.langchain.com/) for seamless language model integration.
- [OpenAI](https://openai.com/) for powerful AI models.
- [FAISS](https://github.com/facebookresearch/faiss) for efficient vector search.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
```

Replace `yourusername` with your GitHub username before uploading.
