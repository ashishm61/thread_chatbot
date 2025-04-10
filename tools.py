import os
import glob

def document_content(doc_type):
    documents_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documents")
    
    if not os.path.exists(documents_dir):
        return ""
    
    txt_files = []
    
    if doc_type == "sales":
        txt_files.extend(glob.glob(os.path.join(documents_dir, "*.txt")))
    
    type_dir = os.path.join(documents_dir, doc_type)
    if os.path.exists(type_dir):
        txt_files.extend(glob.glob(os.path.join(type_dir, "*.txt")))
    
    if not txt_files:
        return ""
    
    all_content = []
    for file_path in txt_files:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                if content:
                    file_name = os.path.basename(file_path)
                    all_content.append(f"--- {doc_type.capitalize()} Report: {file_name} ---\n\n{content}")
        except:
            pass
    
    return "\n\n".join(all_content)

def sales_report_content():
    return document_content("sales")

def hr_report_content():
    return document_content("hr")

def finance_report_content():
    return document_content("finance")

def marketing_report_content():
    return document_content("marketing")
