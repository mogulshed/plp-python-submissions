import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for URLs (can handle multiple)
    urls = input("Please enter one or more image URLs (comma-separated): ").split(',')

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    downloaded_hashes = set()  # To avoid duplicates based on content hash

    for url in [u.strip() for u in urls if u.strip()]:
        try:
            # Fetch the image with timeout and error handling
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Check for important headers (content type)
            content_type = response.headers.get("Content-Type", "")
            if "image" not in content_type:
                print(f"✗ Skipped: {url} (Not an image - Content-Type: {content_type})")
                continue

            # Extract filename from URL or create one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            # Prevent duplicate downloads by comparing content hash
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print(f"✗ Duplicate skipped: {filename}")
                continue

            downloaded_hashes.add(file_hash)

            # Save file to Fetched_Images directory
            filepath = os.path.join("Fetched_Images", filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP Error for {url}: {e}")
        except requests.exceptions.Timeout:
            print(f"✗ Timeout while connecting to {url}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error for {url}: {e}")

    print("Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
