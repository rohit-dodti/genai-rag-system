# GenAI RAG System — In Progress

A modular Python project being developed to explore document ingestion
and Retrieval-Augmented Generation (RAG).

## Current Implementation

The PDF ingestion module uses PyMuPDF to:

- Extract text from each page
- Preserve the source path and file name
- Record the file type and page number
- Return page content alongside its metadata

## Project Structure

| File | Current Status |
|---|---|
| `src/ingestion.py` | PDF text extraction and metadata capture implemented |
| `src/chunking.py` | Placeholder for document splitting |
| `src/embeddings.py` | Placeholder for embedding generation |
| `src/retrieval.py` | Placeholder for document retrieval |
| `src/generation.py` | Placeholder for answer generation |
| `main.py` | Placeholder for pipeline orchestration |

Sample files are organized under `data/raw/`, including PDF, text,
CSV, Excel and JSON files. Only PDF ingestion is currently implemented.

## Run the PDF Ingestion Module

From the repository root, install PyMuPDF:

    python -m pip install pymupdf

Then run:

    python -m src.ingestion

The script reads PDFs from `data/raw/pdf` and prints extracted text
previews and metadata.

Execution has not been recently verified.

## Planned Pipeline

1. Load documents and capture metadata
2. Split text into overlapping chunks
3. Generate embeddings
4. Index and retrieve relevant chunks
5. Generate answers using retrieved context
6. Return source references

## Technologies

Currently implemented:

- Python
- PyMuPDF
- pathlib

Planned:

- Text splitting
- Embedding models
- Vector search
- LLM integration

## Current Limitations

- End-to-end question answering is not implemented.
- Non-PDF loaders are not implemented.
- Scanned PDFs require an additional OCR workflow.
- Automated tests and retrieval evaluation are not included.

## Project Status

Learning project under active development, currently at the PDF
ingestion stage.
