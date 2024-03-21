# 3GPP Data Preparation And Data Insert

The data preparation process refers to extracting relevant pieces of text from the source file format DOCX while preserving basic layout elements such as headers and tables.

The extracted text is then used to generate source data embeddings representations.

The output of the preparation process is project own file format as JSON, containing metadata, a content list, original text content, and embeddings.

These JSON files are then used to execute data insertion while maintaining the relational structure of the text chunks.

## Introduction of the repository

### 1_mkd_from_docx

the folder contains Bash scripts used to convert the word file to markdown file.

- **converttomkd.sh**
    This shell script utilizes the pandoc command-line tool for converting docx to markdown. 

- **organize_files.sh**
    This shell script is to organize Markdown files into subdirectories based on their filenames, utilizing basic file manipulation commands in Bash.

### 2_Json_chunks

This folder contains Python scripts used to split the markdown file based on headers to create context-aware text chunks (paragraph level).

Subsequently, it generates and inserts the corresponding embeddings into the same JSON file.

It also includes a script that utilizes fixed-size recursive chunking with overlapping. This is useful in cases where chunk sizes are more relevant than individual topic sizes.

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

  _The Json Output of the preparation process_

  ```json
  metadata_list	[…]
  content_list	[…]
  title	"3GPP TS 38.304"
  author	"MCC Support"
  version	"V18.0.0"
  subject	"NR; User Equipment (UE) …tive state (Release 18)"
  embeddings	[…]
  ```

### 3_data_insert
the folder contains Python scripts used to create databse collection and insert the data from Json files to databse.

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
