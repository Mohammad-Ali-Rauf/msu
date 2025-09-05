import json
import os
from collections import Counter

# Paths
INPUT_PATH = "./content/stories_with_tokens.json"
FREQ_OUTPUT_PATH = "./content/token_frequencies.json"
LEXICON_OUTPUT_PATH = "../../core/lexicon/dict.json"

# Load stories
print("⏳ Loading stories...")
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    stories = json.load(f)
print(f"✅ Loaded {len(stories)} stories")

# Count tokens
print("🔍 Counting tokens...")
token_counter = Counter()
for story in stories:
    tokens = story["Content"]["Tokens"]
    token_counter.update(tokens)
print("✅ Token counting complete")

# Sort tokens by frequency
sorted_tokens = token_counter.most_common()

# Save frequency list
os.makedirs(os.path.dirname(FREQ_OUTPUT_PATH), exist_ok=True)
with open(FREQ_OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(sorted_tokens, f, ensure_ascii=False, indent=4)
print(f"💾 Saved {len(sorted_tokens)} unique tokens to {FREQ_OUTPUT_PATH}")

# Build lexicon skeleton
print("📝 Building lexicon skeleton...")
lexicon = {}

for token, freq in sorted_tokens:
    lexicon[token] = {
        "word": token,
        "root": "",
        "meaning": "",
        "category": "",        # common, academic, poetic, etc.
        "examples": [],
        "notes": "",
        "romanized": "",
        "frequency": freq
    }

# Save lexicon skeleton
os.makedirs(os.path.dirname(LEXICON_OUTPUT_PATH), exist_ok=True)
with open(LEXICON_OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(lexicon, f, ensure_ascii=False, indent=4)

print(f"✅ Lexicon skeleton saved with {len(lexicon)} tokens to {LEXICON_OUTPUT_PATH}")

# Optional preview top 20
print("\nTop 20 tokens:")
for token, freq in sorted_tokens[:20]:
    print(f"{token}: {freq}")
