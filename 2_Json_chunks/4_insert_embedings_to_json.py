import os
from dotenv import load_dotenv
import requests
import openai
import json
import pandas as pd

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def load_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def process_json_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.json'):
            json_path = os.path.join(directory_path, filename)

            json_data = load_json(json_path)

            combined_data_list = []
            metadata_list = json_data.get('metadata_list', [])
            content_list = json_data.get('content_list', [])
            annexes = json_data.get("Annexes", {})

            # Process regular content
            for i in range(min(len(metadata_list), len(content_list))):
                metadata = metadata_list[i]
                content = content_list[i].strip()
                combined_headers = ' '.join(metadata.get(header, '') for header in metadata)
                if content:
                    combined_data = {
                        "metadata": metadata,
                        "combined_content": f"{combined_headers} {content}"
                    }
                    combined_data_list.append(combined_data)

            # Process annexes
            for annex_title, annex_content in annexes.items():
                combined_data_list.append({
                    "metadata": {"Annex Title": annex_title},
                    "combined_content": annex_content
                })


            combined_df = pd.DataFrame(combined_data_list)
   
            

            combined_df['embeddings'] = combined_df['combined_content'].apply(lambda x: get_openai_embeddings(x))
            json_data['embeddings'] = combined_df['embeddings'].tolist()
            with open(json_path.replace('.json', '_with_embeddings.json'), 'w') as output_file:
                json.dump(json_data, output_file)
        



def get_openai_embeddings(input_text):
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "input": input_text,
        "model": "text-embedding-3-large"
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    if 'data' in response_json:
        # Check if the 'embedding' key is present in the first item of the 'data' list
        first_data_item = response_json['data'][0]
        embeddings = first_data_item.get('embedding', [])
    else:
        embeddings = []

    return embeddings




json_directory = '/home/mufida/Documents/3GPP/38_series/json/context_aware'
process_json_files(json_directory)
