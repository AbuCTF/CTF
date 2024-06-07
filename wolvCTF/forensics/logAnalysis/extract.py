import re

# Function to extract URLs from logs
def extract_urls_from_logs(log_file_path):
    urls = set()  # Use a set to avoid duplicate URLs
    with open(log_file_path, 'r') as file:
        logs = file.read()

    # Extract URLs using regular expressions
    url_pattern = r'Host:\s*([\w.-]+)'
    extracted_urls = re.findall(url_pattern, logs)

    # Add extracted URLs to the set
    for url in extracted_urls:
        urls.add(url)

    return list(urls)

# Function to write URLs to a file
def write_urls_to_file(urls, output_file_path):
    with open(output_file_path, 'w') as file:
        for url in urls:
            file.write(url + '\n')

# Main function
def main():
    log_file_path = 'logs.txt'  # Path to the logs file
    output_file_path = 'urls.txt'  # Output file path for URLs

    # Extract URLs from logs
    urls = extract_urls_from_logs(log_file_path)

    # Write URLs to a file
    write_urls_to_file(urls, output_file_path)

    print(f"{len(urls)} URLs extracted and saved to 'urls.txt'.")

if __name__ == "__main__":
    main()
