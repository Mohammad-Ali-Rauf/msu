# import requests
# from bs4 import BeautifulSoup

# url = "https://www.urdupoint.com/kids/category/moral-stories.html"
# response = requests.get(url)

# response

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories = soup.find_all('div')
#     print(stories)
#     # for index, story in enumerate(stories[:100], start=1):
#     #     story_name = story.find('h1').text.strip()
#     #     writer_name = story.find('span', class_='main_span1').text.strip()
#     #     story_content = story.find('div', class_='main_left_text1').text.strip()

#     #     print(f"Story {index}:")
#     #     print(f"Name: {story_name}")
#     #     print(f"Writer: {writer_name}")
#     #     print(f"Content:\n{story_content}\n{'='*50}\n")

# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories = soup.find_all('a', class_='sharp_box')
#     print(stories)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories = soup.find_all('a', class_='sharp_box')

#     for story in stories:
#         href = story.get('href')
#         print(href)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# moral_stories_links=[]

# for i in range(1,10):
#   url = f"https://www.urdupoint.com/kids/category/moral-stories-page{i}.html"
#   response = requests.get(url)
#   if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories = soup.find_all('a', class_='sharp_box')

#     for story in stories:
#         href = story.get('href')
#         print(href)
#         moral_stories_links.append(href)
#   else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# moral_stories_links

# print(len(moral_stories_links))

# for story in moral_stories_links:
#   response = requests.get(story)
#   if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories_description = soup.find_all('p', class_='txt_red')
#     stories_Name = soup.find_all('h2', class_='txt_blue')
#     print(stories_Name)
#     print(stories_description)
#   else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# stories_description_list=[]

# stories_Name_list=[]

# for story in moral_stories_links:
#     response = requests.get(story)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         stories_Name = soup.find_all('h2', class_='txt_blue')
#         stories_description = soup.find_all('p', class_='txt_red')

#         for name in stories_Name:
#             print(name.get_text())
#             stories_Name_list.append(name.get_text())

#         for description in stories_description:
#             print(description.get_text())
#             stories_description_list.append(description.get_text())

#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# stories_description_list

# print(len(stories_Name_list))

# print(len(stories_description_list))

# stories_writer=[]

# for story in moral_stories_links:
#     response = requests.get(story)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         stories_writers = soup.find_all('font')
#         if stories_writers:
#           for writer in stories_writers:
#             print(writer.get_text())
#             stories_writer.append(writer.get_text())
#         else:
#           stories_writer.append('Not Available')
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# stories_writer

# print(len(stories_writer))

# first_para=[]
# second_para=[]

# for story in moral_stories_links:
#     response = requests.get(story)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         justify_divs = soup.find_all('div', {'align': 'justify'})
#         for div in justify_divs:
#             print(div.get_text())
#             first_para.append(div.get_text())
#         center_divs = soup.find_all('div', {'align': 'center'})
#         for div in center_divs:
#             print(div.get_text())
#             second_para.append(div.get_text())

#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# print(len(first_para))

# print(len(second_para))

# i=0
# for story in moral_stories_links:
#     response = requests.get(story)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         center_divs = soup.find_all('div', {'align': 'center'})
#         print("Story number:",i,len(center_divs))
#         for div in center_divs:
#             print(div.get_text())
#             second_para.append(div.get_text())
#         i=i+1

#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# for story in moral_stories_links:
#     response = requests.get(story)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         justify_divs = soup.find_all('div', {'align': 'justify'})
#         for div in justify_divs:
#             print(div.get_text())
#             first_para.append(div.get_text())
#         center_divs = soup.find_all('div', {'align': 'center'})
#         print(center_divs[1].get_text())
#         second_para.append(center_divs[1].get_text())

#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# print(len(first_para))

# print(len(second_para))

# stories_content=[]

# for i in range(len(first_para)):
#   stories_content.append(first_para[i]+second_para[i])

# print(stories_content)

# stories_content[0]

# print(stories_Name_list)

# print(stories_writer)

# print(stories_description_list)

# print(stories_content)

# for i in range(1,10):
#   url = f"https://www.urdupoint.com/kids/category/moral-stories-page{i}.html"
#   response = requests.get(url)
#   if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     stories = soup.find_all('img', class_='hwa')

#     for story in stories:
#         href = story.get('data-src')
#         print(href)
#   else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

# import csv

# # Zip the lists together to iterate over them simultaneously
# data = zip(stories_Name_list, stories_writer, stories_description_list, stories_content)

# # Specify the CSV file path in your Google Drive
# csv_file_path = '/content/stories.csv'

# # Write data to CSV file
# with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
#     # Create a CSV writer object
#     csv_writer = csv.writer(csv_file)

#     # Write header
#     csv_writer.writerow(['StoryName', 'Writer', 'Description', 'FullStory'])

#     # Write data rows
#     csv_writer.writerows(data)

# print(f'Data has been written to {csv_file_path}')

import requests
from bs4 import BeautifulSoup
import json
import os

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
for i in range(1, 5):  # Adjust range to cover enough pages
    url = f"https://www.urdupoint.com/kids/category/moral-stories-page{i}.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        story_links = soup.find_all('a', class_='sharp_box')
        for link in story_links:
            href = link.get('href')
            if href and href not in moral_stories_links:
                moral_stories_links.append(href)
            if len(moral_stories_links) >= 20:
                break
    if len(moral_stories_links) >= 20:
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
                "FullText": full_story
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
