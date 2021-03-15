import json

import ijson
from tqdm.auto import tqdm

keys = ["created_at", "title", "author", "objectID", "url"]

with open("./HNStoriesAll.json") as f:
    with open("./HNStoriesSplit.jsonl", "w") as o:
        objs = ijson.items(f, "item.hits.item")
        for obj in tqdm(objs, total=1333789):
            filtered = {k: v for k, v in obj.items() if k in keys}
            json.dump(filtered, o)
            o.write("\n")
