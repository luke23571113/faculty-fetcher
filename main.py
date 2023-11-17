import requests
from bs4 import BeautifulSoup
import os

# URL of the directory page
url = 'https://www.hw.com/about/Faculty-Staff-Directory'

# Send a request to the URL
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find divs with class 'image' and then find img tags within those divs
divs = soup.find_all('div', class_='image')
images = [div.find('img') for div in divs]

# Create a directory to save images
os.makedirs('hw_images', exist_ok=True)

# Download each image
for img in images:
    if img:  # Check if img tag exists
        img_url = img['src']  # Get the image URL
        img_response = requests.get(img_url)
        img_name = img_url.split('/')[-1]
        with open(f'hw_images/{img_name}', 'wb') as file:
            file.write(img_response.content)
