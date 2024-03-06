import os
from docx import Document
import json

def extract_metadata(docx_path):
    doc = Document(docx_path)

    metadata = {
        'title': doc.core_properties.title,
        'author': doc.core_properties.author,
        'subject': doc.core_properties.subject,
        #'keywords': doc.core_properties.keywords,
    }

    return metadata

def iterate_docx_files(directory_path, json_directory):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.docx'):
            docx_path = os.path.join(directory_path, filename)

            # Extract metadata
            metadata = extract_metadata(docx_path)

            print(f"File: {os.path.basename(docx_path)}")
            print("Metadata:")
            for key, value in metadata.items():
                print(f"  {key}: {value}")
            print("-" * 30)

            # Update corresponding JSON files
            json_filename = os.path.splitext(filename)[0] + '.json'
            json_path = os.path.join(json_directory, json_filename)

            if os.path.isfile(json_path):
                # Read existing JSON content
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    existing_data = json.load(json_file)

                # Add or update metadata in the JSON data
                existing_data.update(metadata)

                # Write the updated JSON content back to the file
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=2)

                print(f"Updated JSON file: {os.path.basename(json_path)}")
                print("-" * 30)

# Example usage:
docx_directory = '/home/mufida/Documents/3GPP/38_series/docx'
json_directory = '/home/mufida/Documents/3GPP/38_series/json/context_aware'
iterate_docx_files(docx_directory, json_directory)
