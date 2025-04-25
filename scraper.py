# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "selenium",
#     "selenium-stealth",
# ]
# ///
from multiprocessing.managers import ListProxy, SyncManager
from typing import List, Tuple
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from multiprocessing import Pool, Manager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth


def scrape_site(args) -> List:
    url, base_url, visited = args

    if url in visited:
        return []

    visited.append(url)
    options = Options()
    options.add_argument("--headless")  # optional, remove for GUI
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    try:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        print(f"Scraping: {url}")
        with open("manim_docs.txt", "a", encoding="utf-8") as f:
            f.write(soup.get_text())

        next_urls = []
        for link in soup.find_all("a", href=True):
            next_url = urljoin(base_url, link["href"])
            if urlparse(next_url).netloc == urlparse(base_url).netloc and next_url not in visited:
                next_urls.append(next_url)
        return next_urls
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return []
    finally:
        driver.quit()


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
        args: List[Tuple[str, str, ListProxy[str]]] = [
            (url, base_url, visited) for url in to_scrape
        ]
        results = pool.map(scrape_site, args)
        to_scrape: List = list(
            set(url for sublist in results for url in sublist if url not in visited)
        )
    pool.close()
    pool.join()
