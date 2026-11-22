import json

def store_json(raw_data: dict[dict], path: str = "raw.json") -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, ensure_ascii=False, indent=4)

def load_json(path: str = "raw.json") -> dict[dict]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)