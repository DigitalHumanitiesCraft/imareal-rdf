import fitz
from langchain.docstore.document import Document

def load_pdf(files="data/dwp-2019-31.pdf"):
    documents = []
    for file_path in files if isinstance(files, list) else [files]:
        doc = fitz.open(file_path)
        text = "".join(page.get_text("text") for page in doc)
        text = clean_extra_whitespace(text)
        text = group_broken_paragraphs(text)
        documents.append(Document(page_content=text, metadata={"source": file_path}))
    return documents