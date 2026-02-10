# Smart Q&A

A production-ready Retrieval-Augmented Generation (RAG) application that enables natural language question answering over PDF documents. The system processes uploaded PDFs, generates vector embeddings using FAISS, and leverages a sophisticated retrieval and large language model pipeline to provide accurate, context-aware answers based on the document corpus.

---

## Table of Contents

- [Overview](#overview)
- [Technical Architecture](#technical-architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Local Installation and Setup](#local-installation-and-setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [API and Environment Variables](#api-and-environment-variables)
- [Troubleshooting](#troubleshooting)
- [Development Guidelines](#development-guidelines)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Smart Q&A is an intelligent document processing system that combines modern NLP techniques with vector databases to provide accurate answers from your PDF documents. Built with LangChain, FAISS, and GROQ API, it offers a user-friendly Gradio interface for seamless interaction.

**Key Capabilities:**
- Multi-document PDF processing and indexing
- Vector-based semantic search using FAISS
- Context-aware answer generation using LLaMA 3.3 70B
- Persistent knowledge base with automatic state management
- Real-time document processing and querying

---

## Technical Architecture

The application follows a modular architecture with the following components:

1. **Frontend Layer**: Gradio-based web interface for user interactions
2. **Processing Layer**: PDF parsing and document chunking using PyPDF
3. **Embedding Layer**: Sentence transformers (all-MiniLM-L6-v2) for vector generation
4. **Storage Layer**: FAISS vector database for efficient similarity search
5. **Inference Layer**: GROQ API with LLaMA 3.3 70B for answer generation

**Technology Stack:**
- Python 3.10+
- LangChain & LangChain Community
- HuggingFace Sentence Transformers
- FAISS (Facebook AI Similarity Search)
- GROQ API (LLaMA 3.3 70B Versatile)
- Gradio for UI
- PyPDF for document parsing

---

## Features

- **Multi-PDF Support**: Upload and process multiple PDF documents simultaneously
- **Intelligent Chunking**: Automatic page-level document splitting with metadata preservation
- **Vector Storage**: Persistent FAISS index for fast similarity searches
- **Semantic Retrieval**: Context-aware document retrieval with configurable search depth
- **LLM Integration**: State-of-the-art language model for natural language understanding
- **Knowledge Base Management**: Easy reset and rebuild capabilities
- **File Size Validation**: Built-in checks for document size limits (15MB default)
- **Session Persistence**: Vector store survives application restarts
- **Lazy Loading**: Optimized imports for faster startup times

---

## Prerequisites

Before setting up the application, ensure you have the following installed:

### Required Software

1. **Python 3.10 or newer** (Python 3.10 recommended)
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Git** (for version control)
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify installation: `git --version`

3. **pip** (Python package manager)
   - Usually comes with Python
   - Verify installation: `pip --version`

### API Requirements

- **GROQ API Key**: Required for LLM functionality
  - Sign up at [console.groq.com](https://console.groq.com)
  - Generate an API key from the dashboard

### System Requirements

- **Operating System**: Windows 10/11, Linux, or macOS
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: At least 2GB for dependencies and vector storage
- **Internet Connection**: Required for initial setup and API calls

---

## Local Installation and Setup

Follow these steps to set up the application on your local machine:

### Step 1: Clone the Repository

```bash
git clone https://github.com/Srivardhan04/Smart-Q-A.git
cd Smart-Q-A
```

### Step 2: Create a Virtual Environment

Creating a virtual environment isolates project dependencies from your system Python.

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
.\venv\Scripts\activate.bat
```

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal indicating the virtual environment is active.

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencies installed:**
- `gradio` - Web UI framework
- `langchain` - LLM orchestration framework
- `langchain-community` - Community integrations
- `langchain-groq` - GROQ API integration
- `langchain-huggingface` - HuggingFace embeddings
- `sentence-transformers` - Embedding models
- `faiss-cpu` - Vector similarity search
- `python-dotenv` - Environment variable management
- `pypdf` - PDF parsing library

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
# On Windows
echo GROQ_API_KEY=your_actual_groq_api_key_here > .env

# On Linux/macOS
echo "GROQ_API_KEY=your_actual_groq_api_key_here" > .env
```

**Alternatively**, create the file manually:

1. Create a new file named `.env` in the project root
2. Add the following line:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
3. Replace `your_actual_groq_api_key_here` with your actual GROQ API key
4. Save the file

**Important**: Never commit the `.env` file to version control. It should be listed in `.gitignore`.

---

## Configuration

### Application Settings

Key configuration parameters can be modified in the source files:

**In `main.py`:**
```python
MAX_FILE_SIZE_MB = 15  # Maximum PDF file size in megabytes
UPLOAD_DIR = "uploaded_docs"  # Directory for uploaded PDFs
```

**In `rag_pipeline.py`:**
```python
LLM_MODEL = "llama-3.3-70b-versatile"  # GROQ model to use
VECTOR_DB_PATH = BASE_DIR / "vector_store"  # Vector database location
```

**Retriever Settings:**
```python
search_kwargs={"k": 8}  # Number of document chunks to retrieve
```

**Embedding Model:**
```python
model_name="sentence-transformers/all-MiniLM-L6-v2"
```

---

## Running the Application

### Start the Server

From the project root directory with the virtual environment activated:

```bash
python main.py
```

**Expected Output:**
```
Running on local URL:  http://127.0.0.1:7860
```

### Access the Web Interface

1. Open your web browser
2. Navigate to: `http://127.0.0.1:7860` or `http://localhost:7860`
3. The Smart Q&A interface should load

### Stopping the Server

Press `Ctrl+C` in the terminal where the application is running.

---

## Usage Guide

### Uploading and Processing PDFs

1. **Select PDFs**: Click the "Upload PDFs" area and select one or more PDF files
2. **Process Documents**: Click the "Process PDFs" button
3. **Wait for Confirmation**: The status field will display a success message
4. **Verification**: Your documents are now indexed in the vector store

**File Requirements:**
- Format: PDF (.pdf extension)
- Maximum size: 15MB per file (configurable)
- Content: Text-based PDFs (scanned documents may not work optimally)

### Asking Questions

1. **Enter Question**: Type your question in the "Ask a question" text field
2. **Submit Query**: Click the "Get Answer" button
3. **Review Answer**: The answer will appear in the "Answer" text area below
4. **Context-Aware**: Answers are generated based on the uploaded document corpus

**Tips for Better Results:**
- Ask specific, clear questions
- Reference terms or concepts from your documents
- Questions should be answerable from the uploaded PDFs
- Use natural language

### Clearing the Knowledge Base

1. Click the "Clear Knowledge Base" button
2. This action will:
   - Delete the FAISS vector index
   - Remove all uploaded PDF files
   - Reset the application to initial state
3. You must re-upload and process documents to ask new questions

---

## Project Structure

```
Smart-Q-A/
│
├── main.py                 # Gradio UI and application entry point
├── rag_pipeline.py         # RAG logic, vector store, LLM integration
├── requirements.txt        # Python package dependencies
├── .env                    # Environment variables (not in git)
├── README.md              # Project documentation
├── log.txt                # Application logs
│
├── uploaded_docs/         # Temporary storage for uploaded PDFs
│   └── [user_pdfs.pdf]
│
├── vector_store/          # FAISS vector database persistence
│   ├── index.faiss        # FAISS index file
│   └── index.pkl          # FAISS metadata
│
├── assets/                # Static assets (if any)
│
└── __pycache__/           # Python bytecode cache
```

### Key Files Description

**`main.py`**
- Gradio interface setup
- File upload handling and validation
- PDF processing orchestration
- Knowledge base management UI

**`rag_pipeline.py`**
- PDF document loading and splitting
- Vector embeddings generation
- FAISS index creation and management
- Retriever configuration
- LLM integration and prompt engineering
- Question answering logic

**`requirements.txt`**
- All Python package dependencies with compatible versions

**`.env`**
- Secure storage for API keys and sensitive configuration
- Not tracked in version control

---

## API and Environment Variables

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | API key for GROQ LLM service | `gsk_...` |

### Optional Configuration

You can set additional environment variables if needed:

```bash
# Example: Override default model
LLM_MODEL=llama-3.1-8b-instant

# Example: Custom vector store path
VECTOR_DB_PATH=/path/to/custom/vector_store
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Application fails to start

**Solution:**
1. Verify virtual environment is activated: `(venv)` should appear in terminal
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version: `python --version` (should be 3.10+)

#### Issue: "GROQ_API_KEY not found" error

**Solution:**
1. Verify `.env` file exists in project root
2. Check the file contains: `GROQ_API_KEY=your_key_here`
3. Ensure no spaces around the `=` sign
4. Restart the application after creating/modifying `.env`

#### Issue: "FileNotFoundError: No PDFs processed yet"

**Solution:**
1. Upload at least one PDF through the interface
2. Click "Process PDFs" and wait for confirmation
3. Ensure PDFs are text-based, not scanned images

#### Issue: ImportError or ModuleNotFoundError

**Solution:**
1. Activate virtual environment
2. Run: `pip install --upgrade pip`
3. Run: `pip install -r requirements.txt --force-reinstall`

#### Issue: FAISS installation fails on Windows

**Solution:**
1. Install Visual C++ Build Tools
2. Use pre-built wheels: `pip install faiss-cpu --no-cache-dir`
3. Alternatively, use WSL (Windows Subsystem for Linux)

#### Issue: Slow startup time

**Explanation:** First-time model downloads and lazy imports may cause delays.

**Solution:**
1. Be patient during first run (downloading embedding models)
2. Subsequent starts will be faster
3. Models are cached locally after first download

#### Issue: Port 7860 already in use

**Solution:**
```python
# Modify main.py to use a different port
app.launch(server_port=7861)
```

---

## Development Guidelines

### Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Keep functions focused and modular
- Add docstrings to all functions

### Testing

Before committing changes:
1. Test PDF upload and processing
2. Verify question answering functionality
3. Test knowledge base clearing
4. Check error handling

### Git Workflow

1. Create feature branches: `git checkout -b feature-name`
2. Make incremental commits with clear messages
3. Test thoroughly before merging
4. Keep commits atomic and focused

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the Repository**
   ```bash
   # Click 'Fork' on GitHub, then:
   git clone https://github.com/your-username/Smart-Q-A.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests if applicable

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: detailed description of your changes"
   ```

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Provide a clear description of changes

### Contribution Areas

- Bug fixes and error handling improvements
- Additional document format support (DOCX, TXT, etc.)
- Enhanced UI/UX features
- Performance optimizations
- Documentation improvements
- Test coverage expansion

---

## License

This project is open source and available for educational and commercial use.

---

## Support and Contact

For issues, questions, or contributions:
- Open an issue on GitHub: [Smart-Q-A Issues](https://github.com/Srivardhan04/Smart-Q-A/issues)
- Review documentation in this README
- Check troubleshooting section for common problems

---

**Built with LangChain, FAISS, and GROQ API**

Contributions welcome — open an issue or PR with a clear description of the change.
