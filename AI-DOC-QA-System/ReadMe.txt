AI Document QA System (RAG)

##########################################################

Overview

The AI Document QA System is a Retrieval-Augmented Generation (RAG) project that allows users to ask natural language questions and get accurate answers directly from uploaded documents. This system combines semantic search using embeddings with a Large Language Model (LLM) to produce context-aware answers.

Instead of relying solely on the LLM’s training knowledge, this system retrieves relevant information from user-provided documents, making it ideal for company knowledge bases, research papers, or PDF reports.

###########################################################

Features

PDF Ingestion: Reads multiple PDFs from a folder and extracts text automatically.

Semantic Embeddings: Converts document text into vector embeddings using Sentence Transformers for meaningful similarity comparisons.

PostgreSQL Storage: Stores both document text and embeddings in a PostgreSQL database.

RAG Retrieval: Finds the most relevant documents for a user query using cosine similarity.

LLM Integration: Sends retrieved documents to Google Gemini LLM to generate accurate and context-aware answers.

Jupyter Notebook Workflow: Fully reproducible with notebook-based code for ingestion, embedding, database storage, retrieval, and querying.

###################################################

Tech Stack

Python – Core programming language

Jupyter Notebook – Interactive workflow

pypdf – PDF text extraction

sentence-transformers – Generating embeddings

PostgreSQL – Database to store documents and embeddings

Google Generative AI (Gemini) – Large Language Model for generating answers

NumPy – Vector computations for retrieval

################################################

Usage

Place PDF documents in the data/documents folder.

Set up a PostgreSQL database (e.g., rag_db) and update credentials in database.py.

Configure the Google Generative AI API key in the notebook.

Run the Jupyter notebook cells sequentially to:

Load PDFs

Generate embeddings

Store in the database

Query the LLM and get answers

#######################################################

Example Question: What is AI? Answer: Machine Learning is a key area of AI that involves algorithms allowing computers to learn from data.

#######################################################

Future Improvements

Document chunking: Split large PDFs into smaller chunks for more accurate retrieval.

Vector database: Use a dedicated vector DB (e.g., FAISS, Pinecone) for faster retrieval.

Web interface: Build a Flask or Streamlit UI for interactive question answering.

Multi-format support: Extend to DOCX, TXT, or other document types.

##########################################################

License

MIT License – Feel free to reuse and adapt this code for educational or professional projects.
