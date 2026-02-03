import gradio as gr
import os
import shutil

from rag_pipeline import process_pdf, ask_question, clear_vector_store

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

MAX_FILE_SIZE_MB = 15


def upload_pdfs(files):
    if not files:
        return "❌ Please upload at least one PDF."

    for file in files:
        file_size_mb = os.path.getsize(file) / (1024 * 1024)
        if file_size_mb > MAX_FILE_SIZE_MB:
            return f"❌ {os.path.basename(file)} exceeds {MAX_FILE_SIZE_MB} MB."

        file_path = os.path.join(UPLOAD_DIR, os.path.basename(file))
        shutil.copy(file, file_path)
        process_pdf(file_path)

    return "✅ PDFs uploaded and processed successfully."


def reset_knowledge_base():
    clear_vector_store()
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)
        os.makedirs(UPLOAD_DIR)
    return "🧹 Knowledge base cleared."


with gr.Blocks() as app:

    gr.Markdown(
        "<h1 style='text-align:center;'>Smart Q&A</h1>"
        "<p style='text-align:center;'>Upload one or more PDFs and ask questions</p>"
    )

    pdf_files = gr.File(
        label="Upload PDFs",
        file_types=[".pdf"],
        type="filepath",
        file_count="multiple"
    )

    upload_btn = gr.Button("Process PDFs")
    reset_btn = gr.Button("Clear Knowledge Base")

    status = gr.Textbox(label="Status", interactive=False)

    upload_btn.click(upload_pdfs, pdf_files, status)
    reset_btn.click(reset_knowledge_base, None, status)

    question = gr.Textbox(label="Ask a question")
    ask_btn = gr.Button("Get Answer")
    answer = gr.Textbox(label="Answer", lines=8)

    ask_btn.click(ask_question, question, answer)

app.launch(
    css="""
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }
    """
)
