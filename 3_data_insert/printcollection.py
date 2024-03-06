from pymilvus import Collection
import time

import numpy as np
from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
import pymilvus

sdk_version = pymilvus.__version__
print(f"PyMilvus SDK Version: {sdk_version}")

fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"
num_entities, dim = 3000, 8


connections.connect(
    "default", host=HOST, port=MILVUS_PORT, user=MILVUS_USER, password=MILVUS_PASSWORD
)


print(utility.list_collections())


collection = Collection("NR_NG_RAN")
print("schema:", collection.schema.fields[2])
