from bs4 import BeautifulSoup
import requests

url = "https://www.entsoe.eu/publications/electronic-data-interchange-edi-library/"
search_text = "EIC data exchange"  # The constant text

# 1. Get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Find the <a> tag that contains the specific text
# usage of lambda allows for partial matches or exact matches
link = soup.find("a", string=search_text)

# 3. Extract the href and download
if link:
    download_url = link["href"]

    # Handle relative URLs (e.g., "/files/doc.pdf" vs "https://site.com/files/doc.pdf")
    if not download_url.startswith("http"):
        download_url = url + download_url

    print(f"Found URL: {download_url}")

    # Optional: Code to actually download the file
    file_content = requests.get(download_url).content
    with open("xsd_schema.zip", "wb") as f:
        f.write(file_content)
else:
    print("Link with that text not found.")
