#!/usr/bin/env python3
import json, os

# Categories and their set titles
CATEGORIES = {
    "adhikrit": "Section Officer Model Set",
    "kharidar": "Kharidar Model Set", 
    "police": "Police Model Set",
    "subbha": "Subba Model Set",
    "driving": "Driving License Model Set",
    "it": "IT Officer Model Set",
    "nursing": "Nursing Model Set",
}

DIFFICULTIES = ["Easy", "Medium", "Hard", "Easy", "Medium", "Hard", "Easy", "Medium", "Hard", "Easy"]

for cat, title in CATEGORIES.items():
    for lang, lang_dir in [("en", "en"), ("ne", "ne")]:
        tests_path = os.path.join("data", lang_dir, cat, "tests.json")
        if not os.path.exists(tests_path):
            print(f"Skipping {tests_path} - does not exist")
            continue
        
        with open(tests_path, "r", encoding="utf-8") as f:
            tests = json.load(f)
        
        # Update: unlock set3 and set4 for all, keep set5-set10 locked
        for test in tests:
            set_num = int(test["id"].replace("set", ""))
            if set_num <= 2:
                test["locked"] = False
            elif set_num <= 4:
                test["locked"] = False  # Unlock set3 and set4 for newly generated content
            else:
                test["locked"] = True
        
        with open(tests_path, "w", encoding="utf-8") as f:
            json.dump(tests, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {tests_path}")

print("Done updating tests.json files!")
