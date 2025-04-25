# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///
from typing import Set
from requests import get, Response
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited: Set[str] = set()

def scrape_site(url: str, base_url: str) -> None:
    if url in visited:
        return
    
    visited.add(url)
    response: Response = get(url)
    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    print(f"Scraping: {url}")

    with open("manim_docs.txt", "a") as f:
        f.write(soup.get_text())
    
    for link in soup.find_all("a", href=True):
        next_url: str = urljoin(base_url, link["href"])
        if urlparse(next_url).netloc == urlparse(base_url).netloc:
            scrape_site(next_url, base_url)

start_url: str = "https://docs.manim.community/en/stable/"
scrape_site(start_url, start_url)
