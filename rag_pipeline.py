import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
VECTOR_DB_PATH = BASE_DIR / "vector_store"

LLM_MODEL = "llama-3.3-70b-versatile"


def get_embeddings():
    """Lazily initialize embeddings to avoid heavy imports on module import."""
    from langchain_huggingface import HuggingFaceEmbeddings

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def process_pdf(pdf_path: str):
    """Process PDF and append to FAISS (multi-PDF safe)"""
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS

    embeddings = get_embeddings()

    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    if not pages:
        raise ValueError("PDF is empty or unreadable")

    # Strong metadata
    for page in pages:
        page.metadata = {
            "source": os.path.basename(pdf_path),
            "page": page.metadata.get("page", "unknown")
        }

    if VECTOR_DB_PATH.exists():
        vectorstore = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        vectorstore.add_documents(pages)
    else:
        vectorstore = FAISS.from_documents(pages, embeddings)

    vectorstore.save_local(VECTOR_DB_PATH)


def clear_vector_store():
    if VECTOR_DB_PATH.exists():
        shutil.rmtree(VECTOR_DB_PATH)


def load_retriever():
    from langchain_community.vectorstores import FAISS

    if not VECTOR_DB_PATH.exists():
        raise FileNotFoundError("No PDFs processed yet.")

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Force multi-document retrieval
    return vectorstore.as_retriever(
        search_kwargs={"k": 8}
    )


def load_llm():
    from langchain_groq import ChatGroq

    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model=LLM_MODEL,
        temperature=0
    )


def ask_question(question: str) -> str:
    if not question.strip():
        return "Please enter a valid question."

    try:
        retriever = load_retriever()
        llm = load_llm()

        from langchain_core.prompts import PromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.runnables import RunnablePassthrough

        # Multi-PDF aware prompt
        prompt = PromptTemplate.from_template(
            """
You are a Smart Document Q&A assistant.

Multiple PDFs may be provided.
Each context chunk includes a 'source' field indicating the PDF name.

Instructions:
- Use ALL relevant documents.
- Compare information across documents when asked.
- Clearly mention which PDF(s) the answer comes from.
- If a concept appears only in one PDF, explicitly state that.
- If information from a PDF is missing, say so clearly.

Context:
{context}

Question:
{question}

Answer:
"""
        )

        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        return rag_chain.invoke(question)

    except Exception as e:
        return f"Error: {str(e)}"
