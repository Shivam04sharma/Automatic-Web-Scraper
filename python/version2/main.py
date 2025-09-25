import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import random
import threading
import tkinter as tk
from tkinter import scrolledtext

#global domain set
visited_domains = set()  

#Fetch pages
async def fetch(session, url, output_widget):
    try:
        async with session.get(url, timeout=10) as response:
            html = await response.text(encoding='utf-8', errors='ignore')
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string if soup.title else "No title"
            output_widget.insert(tk.END, f"Fetched: {url} | Title: {title}\n")
            output_widget.see(tk.END)

            #collect new links
            links = []
            for a in soup.find_all("a", href=True):
                href = urljoin(url, a['href'])
                domain = urlparse(href).netloc
                if domain not in visited_domains and href.startswith("http"):
                    links.append(href)
            return html, links
    except Exception as e:
        output_widget.insert(tk.END, f"Failed {url}: {e}\n")
        output_widget.see(tk.END)
        return None, []

#crawl pages until target_count unique domains fetched
async def crawl(seed_urls, target_count, output_widget):
    global visited_domains
    visited_domains.clear()
    queue = list(seed_urls)

    async with aiohttp.ClientSession() as session:
        while queue and len(visited_domains) < target_count:
            url = queue.pop(0)
            domain = urlparse(url).netloc
            if domain in visited_domains:
                continue
            html, links = await fetch(session, url, output_widget)
            if html:
                visited_domains.add(domain)
                random.shuffle(links)
                queue.extend(links)

    output_widget.insert(tk.END, f"\n Total unique domains fetched: {len(visited_domains)}\n")
    output_widget.see(tk.END)


def run_scraper():
    seed_input = seed_entry.get().strip()
    seed_urls = [u.strip() for u in seed_input.split(",") if u.strip()]
    if not seed_urls:
        output_widget.insert(tk.END, "Enter at least one seed URL.\n")
        return

    try:
        target_count = int(pages_entry.get())
        if target_count <= 0:
            output_widget.insert(tk.END, "Enter a positive number of pages.\n")
            return
    except ValueError:
        output_widget.insert(tk.END, "Invalid input! Enter an integer.\n")
        return

    threading.Thread(target=lambda: asyncio.run(crawl(seed_urls, target_count, output_widget)), daemon=True).start()

def clear_output():
    output_widget.delete('1.0', tk.END)

# Tkinter UI
root = tk.Tk()
root.title("Automatic Web Scraper")

tk.Label(root, text="Seed URLs (comma-separated):").pack(pady=5)
seed_entry = tk.Entry(root, width=60)
seed_entry.insert(0, "https://www.wikipedia.org/, https://www.python.org/") #default url
seed_entry.pack(pady=5)

tk.Label(root, text="Number of pages to fetch:").pack(pady=5)
pages_entry = tk.Entry(root, width=10)
pages_entry.insert(0,0)  # default num
pages_entry.pack(pady=5)

tk.Button(root, text="Start Scraper", command=run_scraper).pack(pady=5)
tk.Button(root, text="Clear Output", command=clear_output).pack(pady=5)

output_widget = scrolledtext.ScrolledText(root, width=80, height=25)
output_widget.pack(pady=10)

root.mainloop()








# you can use it just for References more links:

# https://www.python.org/
# https://www.wikipedia.org/
# https://www.example.com/
# https://www.djangoproject.com/
# https://www.realpython.com/
# https://www.openai.com/
# https://www.w3schools.com/
# https://www.tutorialspoint.com/
# https://www.mozilla.org/
# https://www.stackoverflow.com/
