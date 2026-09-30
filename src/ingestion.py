import fitz
import pymupdf
from pathlib import Path


PDF_DIRECTORY = Path("data/raw/pdf")


def load_pdf(pdf_path):
    """Extract text and metadata from a PDF."""
    
    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        pages.append({
            "content": text,
            "metadata": {
                "source": str(pdf_path),
                "file_name": pdf_path.name,
                "file_type": "pdf",
                "page_number": page_number
            }
        })

    document.close()

    return pages


if __name__ == "__main__":

    pdf_files = list(PDF_DIRECTORY.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF files")

    for pdf_file in pdf_files:

        print(f"\nProcessing: {pdf_file.name}")

        documents = load_pdf(pdf_file)

        print(f"Pages extracted: {len(documents)}")

        for document in documents:
            print("\n--- Page ---")
            print(document["content"][:500])
            print("\nMetadata:")
            print(document["metadata"])