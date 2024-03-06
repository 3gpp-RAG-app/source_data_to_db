import re
from langchain_text_splitters import MarkdownHeaderTextSplitter
import os
import json


def clean_content(content):
    table_pattern = re.compile(r"\|([^|]+)\|", re.DOTALL)
    line_pattern1 = re.compile(r"\+[+-]+\+")
    line_pattern2 = re.compile(r"\+[+=]+\+")
    line_pattern3 = re.compile(r"[-]{3,}")
    combined_pattern = re.compile(
        f"({table_pattern.pattern})|({line_pattern1.pattern})|({line_pattern2.pattern})|({line_pattern3.pattern})"
    )
    cleaned_content = combined_pattern.sub("", content)
    return cleaned_content


def process_markdown_file(folder, markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        markdown_document = file.read()

    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )
    md_header_splits = markdown_splitter.split_text(markdown_document)

    metadata_list = []
    content_list = []

    for i, item in enumerate(md_header_splits, start=0):
        metadata = item.metadata
        content = item.page_content

        cleaned_content = clean_content(content)

        metadata_list.append(metadata)
        content_list.append(cleaned_content)

    split_info = {
        "metadata_list": metadata_list,
        "content_list": content_list,
    }

    annexes_path = os.path.join(folder, "annexes")
    if not os.path.isdir(annexes_path):
        return

    file_list = os.listdir(annexes_path)

    for file_name in file_list:
        if file_name.lower().endswith(".md"):
            file_path = os.path.join(annexes_path, file_name)

            with open(file_path, "r", encoding="utf-8") as file:
                markdown_content = file.read()
                markdown_content = clean_content(markdown_content)
                annex_name = os.path.splitext(file_name)[0]

                # Append annex_name to metadata_list
                metadata_list.append({"Annex Title": annex_name})

                # Append cleaned content to content_list
                content_list.append(markdown_content)

    base_name = os.path.splitext(os.path.basename(markdown_file))[0]
    output_file = os.path.join(folder, f"{base_name}.json")

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(split_info, json_file, ensure_ascii=False, indent=2)

    print(f"Saved splits to a single JSON file: {output_file}.")


def process_markdown_files_in_directory(root_directory):
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".md"):
                markdown_file = os.path.join(foldername, filename)
                process_markdown_file(foldername, markdown_file)


# Specify the root directory containing the Markdown files in subfolders
root_directory = "/home/mufida/Documents/3GPP/38_series/markdown"

# Process all Markdown files in the specified root directory and its subfolders
process_markdown_files_in_directory(root_directory)
