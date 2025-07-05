"""
5-crawl_recursive_internal_links.py
----------------------------------
Recursively crawls a site starting from a root URL, using Crawl4AI's arun_many and a memory-adaptive dispatcher.
At each depth, all internal links are discovered and crawled in parallel, up to a specified depth, with deduplication.
Usage: Set the start URL and max_depth in main(), then run as a script.
"""
import asyncio, os, re
from urllib.parse import urldefrag, urlparse
from crawl4ai import (
    AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode,
    MemoryAdaptiveDispatcher
)

def url_to_hierarchical_filepath(base_dir: str, url: str) -> str:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path.strip('/')
    
    safe_domain = re.sub(r'[\\/*?:"<>|]', '_', domain)
    path_segments = [seg for seg in path.split('/') if seg]
    full_path_parts = [base_dir, safe_domain] + path_segments
    
    if url.endswith('/') or not path_segments:
        dir_path = os.path.join(*full_path_parts)
        filepath = os.path.join(dir_path, "index.md")
    else:
        dir_path = os.path.join(*full_path_parts[:-1])
        filename = f"{full_path_parts[-1]}.md"
        filepath = os.path.join(dir_path, filename)
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    return filepath

async def crawl_recursive_batch(start_urls, max_depth=3, max_concurrent=10):
    
    output_dir = "crawled_markdown" #Puede ser el nombre que sea
    print(f"Los archivos Markdown se guardarán en la carpeta: '{output_dir}/'")
    
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        stream=False
    )
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,      # Don't exceed 70% memory usage
        check_interval=1.0,                 # Check memory every second
        max_session_permit=max_concurrent   # Max parallel browser sessions
    )

    # Track visited URLs to prevent revisiting and infinite loops (ignoring fragments)
    visited = set()
    def normalize_url(url):
        # Remove fragment (part after #)
        return urldefrag(url)[0]
    current_urls = set([normalize_url(u) for u in start_urls])

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for depth in range(max_depth):
            print(f"\n=== Crawling Depth {depth+1} ===")
            # Only crawl URLs we haven't seen yet (ignoring fragments)
            urls_to_crawl = [normalize_url(url) for url in current_urls if normalize_url(url) not in visited]

            if not urls_to_crawl:
                break

            # Batch-crawl all URLs at this depth in parallel
            results = await crawler.arun_many(
                urls=urls_to_crawl,
                config=run_config,
                dispatcher=dispatcher
            )

            next_level_urls = set()

            for result in results:
                norm_url = normalize_url(result.url)
                visited.add(norm_url)  # Mark as visited (no fragment)
                if result.success:
                    print(f"[OK] {result.url} | Markdown: {len(result.markdown) if result.markdown else 0} chars")
                    # Collect all new internal links for the next depth
                    if result.markdown:
                        filepath = url_to_hierarchical_filepath(output_dir, result.url)
                        try:
                            with open(filepath, 'w', encoding='utf-8') as f: #Toda esa cosota va a ser f
                                f.write(result.markdown)
                            print(f"   -> Guardado en {filepath}")
                        except OSError as e:
                            print(f"   -> [ERROR] No se pudo guardar el archivo {filepath}: {e}")
                    
                    for link in result.links.get("internal", []):
                        next_url = normalize_url(link["href"])
                        if next_url not in visited:
                            next_level_urls.add(next_url)
                else:
                    print(f"[ERROR] {result.url}: {result.error_message}")
                    
            # Move to the next set of URLs for the next recursion depth
            current_urls = next_level_urls

if __name__ == "__main__":
    start_url = ["https://supabase.com/docs/reference/python/start"]
    asyncio.run(crawl_recursive_batch(start_url, max_depth=2 , max_concurrent=10))
    #Se esta copiando de nuevo, la profunidad buena es la 3