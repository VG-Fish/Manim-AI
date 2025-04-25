# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///
from multiprocessing.managers import ListProxy, SyncManager
from typing import List, Set, Tuple
from requests import get, Response
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from multiprocessing import Pool, Manager

def scrape_site(args) -> List:
    url, base_url, visited = args

    if url in visited:
        return []
    
    visited.append(url)
    
    try:
        response: Response = get(url, timeout=10)
        soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
        print(f"Scraping: {url}")

        with open("manim_docs.txt", "a", encoding="utf-8") as f:
            f.write(soup.get_text())
        
        next_urls: List[str] = []
        for link in soup.find_all("a", href=True):
            next_url: str = urljoin(base_url, link["href"])
            if urlparse(next_url).netloc == urlparse(base_url).netloc:
                next_urls.append(next_url)
        return next_urls
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return []

if __name__ == "__main__":
    with open("manim_docs.txt", "w", encoding="utf-8") as f:
        f.close()
    
    start_url: str = "https://docs.manim.community/en/stable/"
    base_url: str = start_url
    manager: SyncManager = Manager()
    visited: ListProxy[str] = manager.list()
    to_scrape: List[str] = [start_url]
    pool = Pool(processes=8)

    while to_scrape:
        args: List[Tuple[str, str, ListProxy[str]]] = [(url, base_url, visited) for url in to_scrape]
        results = pool.map(scrape_site, args)
        to_scrape: List = list(set(url for sublist in results for url in sublist if url not in visited))
    pool.close()
    pool.join()
