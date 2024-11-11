import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def extract_phone_numbers(url):
    try:
        response = requests.get(url, timeout=10)  # Set timeout for faster response
        soup = BeautifulSoup(response.text, 'html.parser')
        phone_numbers = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', soup.get_text())
        return phone_numbers
    except Exception as e:
        return []

domains = [
    "example.com",
    "example2.com",
    "example3.com",
    "example4.com",
    "example5.com"
]

all_phone_numbers = []

# Use ThreadPoolExecutor for concurrent requests to speed up scraping
with ThreadPoolExecutor(max_workers=10) as executor:
    # Submit tasks for each domain
    futures = [executor.submit(extract_phone_numbers, f"http://{domain}") for domain in domains]

    # Gather results
    for future in futures:
        phone_numbers = future.result()
        all_phone_numbers.extend(phone_numbers)

print(all_phone_numbers)
