import os
import json
from PyPDF2 import PdfReader, PdfWriter
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_text_within_range(page, start_y, end_y):
    parts = []

    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if start_y < y < end_y:
            parts.append(text)

    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)
    return text_body


# this part will exclude the header and footer if they are not needed function call to this on text extraction
def extract_text_and_metadata_from_pdf(pdf_path):
    pdf_info = {}
    content_list = []
    chunks_content = []

    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        pdf_info["metadata"] = {
            "title": reader.metadata.title,
            "author": reader.metadata.author,
            "subject": reader.metadata.subject,
            "created_date": reader.metadata.creation_date.isoformat(),
            "num_pages": num_pages,
        }

        foreword_page_index = None

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            if "Foreword\n" in text:
                foreword_page_index = page_num
                break

        if foreword_page_index is not None:
            for page_num in range(2, foreword_page_index):
                page = reader.pages[page_num]
                text = extract_text_within_range(page, 15, 790)
                paragraphs = re.split(r"(\d\n|\d{2,}\n)", text)

                for i in range(0, len(paragraphs) - 1, 2):
                    cleaned_item = re.sub(r"\.{2,}", "", paragraphs[i]).strip()
                    cleaned_page = re.sub(r"\.{2,}", "", paragraphs[i + 1]).strip()

                    if cleaned_item and cleaned_page.isdigit():
                        content_list.append(
                            {"list_item": cleaned_item, "page": int(cleaned_page)}
                        )

        pdf_info["list_of_content"] = content_list

        full_text = ""
        for pages in range(foreword_page_index + 1, num_pages):
            page = reader.pages[pages]
            text = extract_text_within_range(page, 19, 790)
            full_text += text

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000, chunk_overlap=200
        )

        chunks = text_splitter.create_documents([full_text])
        chunks_content.extend([document.page_content for document in chunks])

        pdf_info["chunks_content"] = chunks_content

    return pdf_info


def process_pdfs_in_directory(input_dir, output_dir):
    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, pdf_file)
            result_info = extract_text_and_metadata_from_pdf(pdf_path)

            output_file_path = os.path.join(
                output_dir, pdf_file.replace(".pdf", ".json")
            )
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                json.dump(result_info, output_file, indent=2)

            print(
                f"Text and metadata extracted from {pdf_path} has been saved to {output_file_path}"
            )


input_directory = "/home/mufida/Documents/3GPP/38_series/pdf"
output_directory = "/home/mufida/Documents/3GPP/38_series/json"

process_pdfs_in_directory(input_directory, output_directory)
