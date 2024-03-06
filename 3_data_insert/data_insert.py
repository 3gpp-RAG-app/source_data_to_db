import json
import os
from pymilvus import Collection, connections, utility
from config import HOST, MILVUS_PORT, MILVUS_PORT,MILVUS_USER, MILVUS_PASSWORD

connections.connect(
    "default", host=HOST, port=MILVUS_PORT, user=MILVUS_USER, password=MILVUS_PASSWORD
)
collection = Collection("NR_NG_RAN")

print(utility.list_collections())
collection.flush()
print("collection flushed")


def load_json(json_path):
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def process_json_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".json"):
            json_path = os.path.join(directory_path, filename)

            json_data = load_json(json_path)
            title = json_data.get("title", "")
            version = json_data.get("version", "")
            text_titles = json_data.get("metadata_list", [])
            text = json_data.get("content_list", [])
            embeddings = json_data.get("embeddings", [])

            for i, emb in enumerate(embeddings):
                combined_headers = " ".join(
                    text_titles[i].get(header, "") for header in text_titles[i]
                )
                if len(emb) == 3072:
                    entity = [
                        [i],
                        [f"{title}, V18.0.0"],
                        [combined_headers],
                        [emb],
                        [f"{combined_headers} \n {text[i]}"],
                    ]
                    collection.insert(entity)
                    collection.flush()
                    print(
                        f"inserted {i} from {filename} \nembeddings list len is {len(embeddings)}, dimensions {len(emb)}\ninserted text list is {len(text)}"
                    )
                    collection.release()
                else:
                    pass


if __name__ == "__main__":
    process_json_files("/home/mufida/Documents/3GPP/38_series/json/context_aware")
