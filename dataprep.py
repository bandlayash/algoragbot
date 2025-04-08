import os
from langchain_community.document_loaders import PyPDFLoader 

def load_pdfs_metadata(directory_path):
    documents = []
    for file in os.listdir(directory_path):
        if file.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, file)
            try:
                # Determine document type from filename or folder structure
                doc_type = "unknown"
                if "lecture" in file.lower():
                    doc_type = "lecture"
                elif "hw" in file.lower():
                    if "sol" in file.lower():
                        doc_type = "homework_solution"
                    else:
                        doc_type = "homework"
                elif "review" in file.lower():
                    doc_type = "exam"
                elif "practice" in file.lower():
                    doc_type = "practice_problem"
                    
                # Load PDF
                loader = PyPDFLoader(pdf_path)
                docs = loader.load()
                    
                    # Add metadata to each page
                for doc in docs:
                    doc.metadata["source_type"] = doc_type
                    doc.metadata["filename"] = file
                    
                documents.extend(docs)
                print(f"Loaded: {file} as {doc_type}")
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return documents

print(load_pdfs_metadata("/Users/ybandla/Documents/Code/rag bot/algoragbot/algorithms_docs"))