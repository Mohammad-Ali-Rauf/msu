import json
import os

input_path = './content/stories.json'
output_path = './content/stories_clean.json'

typo_map = {
    "بہی": "بھی",
    "تہا": "تھا",
    "آنکہ": "آنکھ",
    "دیکہ": "دیکھ",
    "ذایقہ": "ذائقہ",
    "کہاتی": "کھاتی",
    "کچہ": "کچھ",
    "لاکہوں": "لاکھوں",
    "پہول": "پھول",
    "ہویی": "ہوئی",
    "بہگا": "بھاگا",
    "کویی": "کوئی",
    "ساتہ": "ساتھ",
    "سونگہ": "سونگھ",
}

def correct_token(token):
    return typo_map.get(token, token)

def clean_stories(data):
    for story in data:
        tokens = story["Content"]["Tokens"]
        story["Content"]["Tokens"] = [correct_token(tok) for tok in tokens]
    return data

def main():
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    # Load raw stories
    with open(input_path, 'r', encoding='utf-8') as infile:
        stories_data = json.load(infile)

    print(f"📂 Loaded {len(stories_data)} stories")

    # Clean the tokens
    cleaned_data = clean_stories(stories_data)

    # Save to new JSON
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(cleaned_data, outfile, ensure_ascii=False, indent=4)

    print(f"✅ Cleaned stories saved to {output_path}")
    print(f"🔧 Corrections applied: {len(typo_map)} typo rules")

if __name__ == "__main__":
    main()
