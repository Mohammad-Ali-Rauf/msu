import json
from collections import Counter
import os

# Path to your big JSON
json_file_path = "./content/stories_clean.json"

# Load the giant JSON file
print("⏳ Loading corpus... this may take a while...")
with open(json_file_path, "r", encoding="utf-8") as f:
    stories = json.load(f)

print(f"✅ Loaded {len(stories)} stories")

# Token frequency counter
token_counter = Counter()

print("🔍 Counting tokens across all stories...")
for story in stories:
    tokens = story["Content"]["Tokens"]
    token_counter.update(tokens)

print("✅ Done counting!")

# Sort by frequency (descending)
sorted_tokens = token_counter.most_common()

# Save full frequency list
freq_file_path = "./content/token_frequencies.json"
os.makedirs(os.path.dirname(freq_file_path), exist_ok=True)

with open(freq_file_path, "w", encoding="utf-8") as f:
    json.dump(sorted_tokens, f, ensure_ascii=False, indent=4)

print(f"📊 Token frequency analysis complete!")
print(f"💾 Saved {len(sorted_tokens)} unique tokens to {freq_file_path}")

# Optional: preview top 20
print("\nTop 20 tokens:")
for token, freq in sorted_tokens[:20]:
    print(f"{token}: {freq}")
