# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "seleniumbase",
# ]
# ///
import os
import time
from multiprocessing import Pool, Manager
from typing import List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from seleniumbase import Driver

def scrape_page(args) -> List[str]:
    """Scrape a single page and return new links discovered"""
    url, base_domain, visited, output_file = args
    
    if url in visited:
        return []
    
    visited.append(url)
    print(f"Scraping: {url}")
    
    driver = Driver(browser="firefox", headless=True)
    new_urls = []
    
    try:
        # Set page load timeout to avoid hanging on slow pages
        driver.set_page_load_timeout(15)
        driver.get(url)
        
        # Wait for page to load
        time.sleep(0.5)
        
        # Get page content
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract text and write to file
        text_content = soup.get_text(separator="\n", strip=True)
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n--- PAGE: {url} ---\n\n")
            f.write(text_content)
        
        # Find all links on the page
        for link in soup.find_all("a", href=True):
            href = link["href"]
            # Skip fragment links, javascript, etc.
            if href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:"):
                continue
                
            next_url = urljoin(url, href)
            
            # Only follow links on the same domain
            if urlparse(next_url).netloc == base_domain and next_url not in visited:
                new_urls.append(next_url)
                
        return new_urls
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
        
    finally:
        driver.quit()

def main():
    # Configuration
    start_url = "https://docs.manim.community/en/stable/"
    output_file = "manim_docs.txt"
    max_pages = 10000
    num_workers = min(8, os.cpu_count() or 4)
    
    # Clear output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Website Scrape: {start_url}\nDate: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Setup multiprocessing resources
    manager = Manager()
    visited = manager.list()
    base_domain = urlparse(start_url).netloc
    
    # Initialize URL queue
    to_visit = [start_url]
    
    # Track statistics
    start_time = time.time()
    pages_scraped = 0
    
    # Create process pool
    with Pool(processes=num_workers) as pool:
        while to_visit and pages_scraped < max_pages:
            # Prepare batch of URLs to process
            batch_size = min(num_workers * 2, len(to_visit), max_pages - pages_scraped)
            current_batch = to_visit[:batch_size]
            to_visit = to_visit[batch_size:]
            
            # Create arguments for each URL
            args = [(url, base_domain, visited, output_file) for url in current_batch]
            
            # Process URLs in parallel
            results = pool.map(scrape_page, args)
            
            # Update statistics
            pages_scraped += len(current_batch)
            
            # Add new URLs to queue
            new_urls = [url for sublist in results for url in sublist if url not in visited]
            to_visit.extend(new_urls)
            
            # Status update
            elapsed = time.time() - start_time
            pages_per_minute = (pages_scraped / elapsed) * 60 if elapsed > 0 else 0
            print(f"Progress: {pages_scraped}/{max_pages} pages | Queue: {len(to_visit)} URLs | Speed: {pages_per_minute:.1f} pages/min")
    
    # Final statistics
    total_time = time.time() - start_time
    print(f"\nScraping completed!")
    print(f"Pages scraped: {pages_scraped}")
    print(f"Total time: {total_time:.1f} seconds")
    print(f"Average speed: {pages_scraped / total_time * 60:.1f} pages per minute")
    print(f"Content saved to: {output_file}")

if __name__ == "__main__":
    main()