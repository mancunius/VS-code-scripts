import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the Gregobase site
base_url = "https://gregobase.selapa.net"

# Directory to save the downloaded files
download_dir = "gabc_files"
os.makedirs(download_dir, exist_ok=True)

# Function to download a file
def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# Function to get all chant detail page links
def get_chant_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    chant_links = []
    
    # Look for links to chant detail pages
    for li in soup.find_all('li'):
        a_tag = li.find('a', href=True)
        if a_tag and 'chant.php?id=' in a_tag['href']:
            full_url = urljoin(base_url, a_tag['href'])
            chant_links.append(full_url)
    
    return chant_links

# Function to get the .gabc file link from a chant detail page
def get_gabc_link(chant_url):
    response = requests.get(chant_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Look for the .gabc file link in the "Download" section
    download_section = soup.find('h4', text='Download')
    if download_section:
        for sibling in download_section.find_next_siblings('ul'):
            for a_tag in sibling.find_all('a', href=True):
                if 'format=gabc' in a_tag['href']:
                    return urljoin(base_url, a_tag['href'])
    
    return None

# Main function to scrape and download
def scrape_and_download():
    # Target the usage.php page with the specific id
    start_url = urljoin(base_url, "usage.php?id=al")
    print(f"Scanning page: {start_url}")
    
    # Get links to chant detail pages
    chant_links = get_chant_links(start_url)
    if not chant_links:
        print("No chant detail pages found.")
        return
    
    print(f"Found {len(chant_links)} chant detail pages. Scanning for .gabc files...")
    
    # Visit each chant detail page and download the .gabc file
    for chant_link in chant_links:
        print(f"Scanning chant page: {chant_link}")
        gabc_link = get_gabc_link(chant_link)
        if gabc_link:
            print(f"Downloading .gabc file: {gabc_link}")
            download_file(gabc_link, download_dir)
        else:
            print("No .gabc file found on this page.")

# Run the script
scrape_and_download()
print("Download complete!")