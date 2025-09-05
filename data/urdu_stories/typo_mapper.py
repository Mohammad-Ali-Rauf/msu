import json
import re
import unicodedata
from collections import Counter

# ------------------ Constants ------------------
URDU_ALPHABETS = frozenset("آ أ ا ب پ ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ؤ ہ ۂ ۃ ھ ء ی ئ ے ۓ".split())
URDU_DIGITS = frozenset("۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹".split())
URDU_PUNCTUATIONS = frozenset("؛ ، ٫ ؟ ۔ ٪ —".split())
URDU_DIACRITICS = frozenset("\u064e \u064B \u0670 \u0650 \u064F \u064d".split())
URDU_EXTRA_CHARACTERS = frozenset("؀ ؁ ؂ ؃ ؍ ؎ ؏ ؐ ؑ ؒ ؓ ؔ ؕ ٌ ّ ْ ٓ ٔ ٖ ٗ ٘ ٬ ٴ".split())
URDU_ALL_CHARACTERS = URDU_ALPHABETS | URDU_DIGITS | URDU_PUNCTUATIONS | URDU_DIACRITICS | URDU_EXTRA_CHARACTERS

typo_map = {
    "بہی": "بھی", "تہا": "تھا", "آنکہ": "آنکھ", "دیکہ": "دیکھ",
    "ذایقہ": "ذائقہ", "کہاتی": "کھاتی", "کچہ": "کچھ", "لاکہوں": "لاکھوں",
    "پہول": "پھول", "ہویی": "ہوئی", "بہگا": "بھاگا", "کویی": "کوئی",
    "ساتہ": "ساتھ", "سونگہ": "سونگھ"
}

EXTRA_NON_URDU = set('“”‘’"\'' + ''.join("0123456789"))
western_to_urdu_digits = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
uncorrected_tokens = set()
token_counter = Counter()

# ------------------ Helper Functions ------------------
def normalize_token(token):
    token = token.strip()
    token = unicodedata.normalize('NFC', token)
    return token

def strip_punctuation(token):
    return ''.join(c for c in token if c not in URDU_PUNCTUATIONS and c not in EXTRA_NON_URDU)

def convert_digits(token):
    return token.translate(western_to_urdu_digits)

def remove_dot_sequences(token):
    return re.sub(r'[․.]{2,}', '', token)

def is_valid_urdu_token(token):
    return all(c in URDU_ALL_CHARACTERS for c in token)

def correct_token(token):
    corrected = typo_map.get(token)
    if corrected:
        return corrected
    if not is_valid_urdu_token(token):
        uncorrected_tokens.add(token)
        token_counter[token] += 1
    return token

def tokenize_and_clean(text):
    text = re.sub(r'\s+', ' ', text)
    raw_tokens = re.split(r"[ \n\r\t،۔؟!,:;«»\"'()\-]+", text)
    tokens = []
    for tok in raw_tokens:
        if not tok.strip():
            continue
        tok = normalize_token(tok)
        tok = strip_punctuation(tok)
        tok = convert_digits(tok)
        tok = remove_dot_sequences(tok)
        tok = correct_token(tok)
        if tok and is_valid_urdu_token(tok):
            tokens.append(tok)
    return tokens

# ------------------ Main ------------------
INPUT_PATH = './content/stories.json'
OUTPUT_PATH = './content/stories_with_tokens.json'

with open(INPUT_PATH, 'r', encoding='utf-8') as f:
    stories = json.load(f)

for story in stories:
    story_text = story["Content"]["FullText"]
    story["Content"]["Tokens"] = tokenize_and_clean(story_text)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(stories, f, ensure_ascii=False, indent=4)

print(f"✅ Tokens populated and cleaned for {len(stories)} stories, saved to {OUTPUT_PATH}")
if uncorrected_tokens:
    print(f"⚠️ Unrecognized tokens: {len(uncorrected_tokens)}")
    for tok, count in token_counter.most_common(20):
        print(f"  - {tok}: {count}")
