# Smart Q&A

Smart Q&A is a lightweight RAG (Retrieval-Augmented Generation) application for asking natural language questions over PDF documents. Upload one or more PDFs, the app converts them into vector embeddings (FAISS), and a retrieval+LLM pipeline answers questions using the uploaded documents as context.

---

## Features ✅

- Upload multiple PDFs through a web UI (Gradio)
- Extracts and splits PDF pages, stores embeddings in a local FAISS vector store
- Uses a retriever + LLM RAG pipeline to answer questions using the documents
- Persistent vector store in `vector_store/` so your knowledge base survives restarts
- Buttons to process PDFs and to clear the knowledge base

---

## Prerequisites ⚙️

- Python 3.10 (recommended) or newer
- Git (for pushing to remote)
- Optional: WSL on Windows if you run into native build issues for some packages

---

## Setup / Installation (Windows)

1. Clone repo (if you haven't already):

   git clone https://github.com/Srivardhan04/Smart-Q-A.git
   cd Smart-Q-A

2. Create & activate a virtual environment:

   python -m venv venv
   PowerShell: & .\venv\Scripts\Activate.ps1
   CMD: .\venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file with your GROQ API key (or export it in your environment):

   GROQ_API_KEY=your_groq_api_key_here

   Note: the app uses the `GROQ_API_KEY` environment variable for the LLM.

---

## Run the app ▶️

Start the Gradio app:

   python main.py

Open http://127.0.0.1:7860 in your browser.

Usage:
- Upload one or more PDFs (max file size default 15 MB each), click "Process PDFs".
- Ask a question in the provided input and click "Get Answer".
- Use "Clear Knowledge Base" to delete the stored FAISS index and uploaded files.

---

## File layout

- `main.py` — Gradio frontend and file upload handlers
- `rag_pipeline.py` — PDF processing, vector store management, retriever, and LLM pipeline
- `vector_store/` — saved FAISS index files
- `uploaded_docs/` — where uploaded PDFs are stored

---

## Troubleshooting & tips 🔧

- If startup is slow or you get long imports, the project uses lazy imports for heavy libraries to allow the UI to start quickly.
- On Windows, installing `faiss-cpu` and `transformers` sometimes requires prebuilt wheels or WSL.
- If you see `FileNotFoundError: No PDFs processed yet.`, upload and process at least one PDF.
- For authentication errors with `git push`, ensure your GitHub credentials or PAT are configured in your system Git credential manager.

---

## Git / Push to GitHub (example commands)

If you want to initialize and push the project to GitHub from this folder (replace the remote URL with yours):

   echo "# Smart-Q-A" >> README.md
   git init
   git add README.md
   git add .
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/Srivardhan04/Smart-Q-A.git
   git push -u origin main

Note: The last command may prompt for credentials or require a configured PAT/SSH key.

---

## Contributing

Contributions welcome — open an issue or PR with a clear description of the change.

---

## License

This project is provided "as-is". Add your preferred license (e.g. MIT) in `LICENSE` if you wish.

---

If you'd like, I can also add a `start` script and automate the steps for creating and pushing the initial commit. Would you like me to run the Git commands now? 📤