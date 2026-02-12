# Intelligent Document QA System

An intelligent question-answering system that leverages **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers .
## Overview

This project uses a modern RAG pipeline to ingest documents, split them into manageable chunks, embed them into a vector store, and retrieve relevant context for answering natural-language questions. It is built with production-grade open-source tools and runs entirely on your local machine — no external API keys required for embeddings.

## Tech Stack

| Component            | Technology                                      |
| -------------------- | ----------------------------------------------- |
| **Framework**        | [LangChain](https://www.langchain.com/)         |
| **Embeddings**       | [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers) |
| **Vector Store**     | [ChromaDB](https://www.trychroma.com/)          |
| **Language**         | Python 3.11                                     |

## Project Structure

```
.
├── main.py                 # Entry point — document ingestion & QA pipeline
├── test.py                 # Unit / integration tests
├── companyPolicies.txt     # Sample document (company policy handbook)
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # You are here
```

## Getting Started

### Prerequisites

- **Python 3.11+** installed on your machine.
- (Optional) A virtual environment tool (`venv`, `conda`, etc.).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kushal9889/intelligent-document-qa-system.git
   cd intelligent-document-qa-system
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate      # macOS / Linux
   # env\Scripts\activate       # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the main application:

```bash
python main.py
```

The script will:

1. Download (or read) the company policies document.
2. Split the document into chunks using `CharacterTextSplitter`.
3. Generate embeddings via HuggingFace Sentence Transformers.
4. Store the embeddings in a local ChromaDB vector store.
5. Accept natural-language questions and return relevant answers.

## How It Works

```
┌──────────────┐     ┌────────────────┐     ┌──────────────┐
│  Documents   │ ──▶ │  Text Splitter │ ──▶ │  Embeddings  │
└──────────────┘     └────────────────┘     └──────┬───────┘
                                                   │
                                                   ▼
┌──────────────┐     ┌────────────────┐     ┌──────────────┐
│   Answer     │ ◀── │   Retriever    │ ◀── │  ChromaDB    │
└──────────────┘     └────────────────┘     └──────────────┘
```

1. **Ingest** — Raw documents are loaded and split into overlapping chunks.
2. **Embed** — Each chunk is converted into a dense vector using a HuggingFace model.
3. **Store** — Vectors are indexed in ChromaDB for fast similarity search.
4. **Retrieve & Answer** — A user query is embedded, the most relevant chunks are retrieved, and an answer is generated.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is open-source. See the [LICENSE](LICENSE) file for details.

## Author

**Kushal Gaddamwar** — [GitHub](https://github.com/Kushal9889)
