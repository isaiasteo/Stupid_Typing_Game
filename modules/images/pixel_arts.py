import json
from pathlib import Path

folder = Path(__file__).parent / "jsons"

pixel_arts = {}

for file in folder.glob("*.json"):
    name = file.stem

    with open(file, "r", encoding="utf-8") as f:
        pixel_arts[name] = json.load(f)
