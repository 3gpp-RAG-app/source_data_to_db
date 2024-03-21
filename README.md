# 3GPP-CHATBOT-DATA-PROCESS

## The project developers

The project is developed by the third-year Information Technology students from Oulu University of Applied Sciences:

- **Antti-Jussi Niku**, [GitHub account](https://github.com/ArunJ0)
- **Mufida Alakulju**, [GitHub account](https://github.com/mufidaA)
- **Yinan Li**, [GitHub account](https://github.com/YinanLi1987)

## Introduction of the repository

This is the data process part of a company-oriented-project, the project aim is to "Define and develop a market-leading 3GPP CR analytics application MVP(minimum viable product)".
This repository includes three folders each responsible for a specific purpose.

- **1_mkd_from_docx**,the script used to convert the word file to mark down file.
- **2_Json_chunks**,the script used to chunk the mark down file into small pices.
- **3_data_insert**,the script used to embedding and inserting the Json file.

## Technologies used in each folder

- 1_mkd_from_docx:

  - **converttomkd.sh**
    This Bash script utilizes the pandoc command-line tool for converting documents. pandoc is a versatile tool capable of converting between various document formats, including Word documents (docx) to Markdown (md). By leveraging pandoc, the script automates the conversion process, making it efficient and convenient.

  - **organize_files.sh**
    This shell script is to organize Markdown files into subdirectories based on their filenames, utilizing basic file manipulation commands in Bash.

- 2_Json_chunks:

  - **1_split_annex.py**
    This Python script utilizes regular expressions and file manipulation functionalities in the os module to split Markdown files based on specified headers.

  - **2_mkd_splitter.py**
    The script aims to split Markdown files based on headers, extracting metadata and content while utilizing regular expressions, the langchain_text_splitters library for Markdown text splitting, and JSON serialization for data storage.

  - **3_add_meta_tp_json.py**
    This script extracts metadata from DOCX files, updates corresponding JSON files with the extracted metadata, utilizing Python's os module for file operations, the docx library for parsing DOCX files, and JSON serialization for data storage.

  - **4_insert_embedings_to_json.py**
    This script processes JSON files, combines metadata and content, retrieves OpenAI embeddings for the combined content, utilizing Python's os, requests, and json modules, as well as OpenAI's API for text embeddings.

  - **json_from_pdf_fixed_size.py**
    This Python script extracts text and metadata from PDF files, splits the text into chunks, and saves the extracted information into JSON files, utilizing the os, json, PyPDF2, and langchain libraries for PDF processing and text splitting.

- 3_data_insert:

  - **creat_collection.py**
    This Python script establishes a connection to Milvus, a vector database, creates a collection with a specified schema, including fields for storing embeddings and text, and creates an index on the embeddings field for efficient similarity search, utilizing the pymilvus library for interaction with Milvus.

  - **data_insert.py**
    This Python script loads JSON files containing metadata, text, and embeddings, and inserts them into a Milvus collection for efficient similarity search, utilizing the pymilvus library to interact with Milvus and json module for JSON file handling.

  - **printcollection.py**
    This Python script demonstrates connection to a Milvus server, lists existing collections, retrieves schema information for a specific collection, and prints the schema fields, utilizing the pymilvus library for interaction with Milvus.

## How to implement the data process

**Step one:**

Ensure you have Python installed on your system.

**Step two:**

Install necessary libraries by running:

- pip install python-docx pymilvus langchain pandoc

**Step three:**

- Convert DOCX Files to Markdown:

  Place all your DOCX files in a directory(`path to your directory containing DOCX files`).
  Run: bash converttomkd.sh

- Organize Markdown files into subdirectories based on their filenames:

  bash organize_files.sh

**Step four:**

- Run the python file in the 2_Json_chunks accordingly to chunk the Markdown file into prepared Json file:

  python 1_split_annex.py
  python 2_mkd_splitter.py
  python 3_add_meta_tp_json.py
  python 4_insert_embedings_to_json.py
  python json_from_pdf_fixed_size.py

**Step five:**

- Create Collection:

  python creat_collection.py

- Insert Data:

  python data_insert.py

- Verify Collection and Schema:

  python printcollection.py
