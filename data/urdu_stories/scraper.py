import requests
from bs4 import BeautifulSoup
import json
import os
import re

# Step A: Normalization
def normalize_urdu(text: str) -> str:
    replacements = {
        "ي": "ی", "ى": "ی", "ئ": "ی", "ے": "ے",
        "ك": "ک", "ٮ": "ب", "ڤ": "ف",
        "ه": "ہ", "ھ": "ہ", "ة": "ہ",
        "ؤ": "و", "إ": "ا", "أ": "ا", "ٱ": "ا",
        "ء": "", "ٓ": "", "ٔ": "", "ٗ": "", "َ": "", "ً": "", "ُ": "", "ٌ": "", "ِ": "", "ٍ": "", "ْ": ""
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

# Step B: Simple tokenization
def tokenize_urdu(text: str):
    text = normalize_urdu(text)
    # Urdu punctuation + Latin
    tokens = re.split(r"[ \n\r\t،۔؟!,:;«»\"'()\-]+", text)
    return [tok.strip() for tok in tokens if tok.strip()]


def extract_story_text(soup):
    content_div = soup.find('div', class_='txt_detail')
    if not content_div:
        return ""

    # Remove only scripts and styles, not all divs
    for tag in content_div.find_all(['script', 'style']):
        tag.decompose()

    # Extract full text with line breaks
    full_text = content_div.get_text(separator='\n', strip=True)

    # Filter out ad markers or empty lines
    lines = [line for line in full_text.split('\n') if line.strip() and not line.strip().startswith('(')]
    return "\n".join(lines)

# Step 1: Get two story links
url = "https://www.urdupoint.com/kids/category/moral-stories.html"
response = requests.get(url)

# Collect story links from multiple pages
moral_stories_links = []
for i in range(1, 20):  # Adjust range to cover enough pages
    url = f"https://www.urdupoint.com/kids/category/moral-stories-page{i}.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        story_links = soup.find_all('a', class_='sharp_box')
        for link in story_links:
            href = link.get('href')
            if href and href not in moral_stories_links:
                moral_stories_links.append(href)
            if len(moral_stories_links) >= 100:
                break
    if len(moral_stories_links) >= 100:
        break

# Step 2: Scrape each story
stories_data = []

for story_url in moral_stories_links:
    response = requests.get(story_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        story_name = soup.find('h2', class_='txt_blue')
        description = soup.find('p', class_='txt_red')
        # Try styled span first
        writer_span = soup.select_one('div.txt_detail span[style*="rgb(255, 0, 0)"]')
        if writer_span and writer_span.get_text(strip=True):
            writer = writer_span.get_text(strip=True)
        else:
            # Fallback: scan for likely writer line in story text
            content_div = soup.find('div', class_='txt_detail')
            writer = "Not Available"
            if content_div:
                lines = list(content_div.stripped_strings)
                for line in lines:
                    if len(line.strip()) <= 30 and "تحریر" not in line and "تحریر نمبر" not in line:
                        writer = line.strip()
                        break

        full_story = extract_story_text(soup)

        story_dict = {
            "StoryName": story_name.get_text(strip=True) if story_name else "No Title",
            "Writer": writer,
            "Description": description.get_text(strip=True) if description else "No Description",
            "Content": {
                "FullText": full_story,
                "Tokens": tokenize_urdu(full_story)
            },
            "URL": story_url
        }

        stories_data.append(story_dict)
    else:
        print(f"Failed to retrieve story at {story_url}. Status code: {response.status_code}")

# Step 3: Save to JSON
json_file_path = './content/stories.json'
os.makedirs(os.path.dirname(json_file_path), exist_ok=True)

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(stories_data, json_file, ensure_ascii=False, indent=4)

print(f"✅ Data for {len(stories_data)} stories saved to {json_file_path}")
