import requests
from urllib.parse import urlparse
import re

# Function to check if a URL is valid and add the scheme if missing
def validate_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == '':
        return 'https://' + url
    return url

# Function to fetch HTML content of a URL and search for a flag
def fetch_and_search_flag(url):
    try:
        url = validate_url(url)
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            if "wctf" in response.text:
                return True
    except Exception as e:
        print(f"Error occurred while checking URL {url}: {e}")
    return False

# Main function
def main():
    urls_file = 'urls.txt'  # Path to the file containing extracted URLs

    # Read URLs from file
    with open(urls_file, 'r') as file:
        urls = file.readlines()

    # Analyze URLs
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        print(f"Analyzing URL: {url}")
        if fetch_and_search_flag(url):
            print(f"ALERT: URL {url} contains a flag!")
            break  # Stop when a flag is found

if __name__ == "__main__":
    main()
