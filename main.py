from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

# Setup Selenium WebDriver
driver = webdriver.Chrome('path_to_chromedriver')
driver.get('https://www.hw.com/about/Faculty-Staff-Directory')

# Find and click the button to load images
button_selector = 'your_button_selector_here'  # Replace with the actual CSS selector of the button
button = driver.find_element_by_css_selector(button_selector)
button.click()

# Wait for content to load
time.sleep(5)

# Get the page source after the content has loaded
html_content = driver.page_source
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
divs = soup.find_all('div', class_='image')
images = [div.find('img') for div in divs]

# Base URL for constructing absolute URLs
base_url = 'https://www.hw.com'

# Create a directory to save images
os.makedirs('hw_images', exist_ok=True)

# Download each image
for img in images:
    if img and img.get('src'):
        img_url = img['src']
        if not img_url.startswith('http'):
            img_url = base_url + img_url
        img_response = requests.get(img_url)
        img_name = img_url.split('/')[-1]
        with open(f'hw_images/{img_name}', 'wb') as file:
            file.write(img_response.content)
