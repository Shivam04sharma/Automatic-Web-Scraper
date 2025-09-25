import asyncio
import aiohttp
import threading
import tkinter as tk
from tkinter import scrolledtext

# Async fetch function
async def fetch(session, url, output_widget):
    async with session.get(url) as response:
        html = await response.text()
        output_widget.insert(tk.END, f"Fetched {url} with {len(html)} chars\n")
        output_widget.see(tk.END)
        return html

# Async main scraper
async def scrape_pages(n, output_widget):
    urls = [f"https://httpbin.org/delay/1?i={i}" for i in range(1, n+1)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, output_widget) for url in urls]
        await asyncio.gather(*tasks)
        output_widget.insert(tk.END, f"\nTotal pages fetched: {len(tasks)}\n")

def run_scraper():
    try:
        n = int(entry.get())
        if n <= 0:
            output.insert(tk.END, "Enter a positive integer!\n")
            return
    except ValueError:
        output.insert(tk.END, "Invalid input! Enter an integer.\n")
        return
    threading.Thread(target=lambda: asyncio.run(scrape_pages(n, output)), daemon=True).start()


def clear_output():
    output.delete('1.0', tk.END)

root = tk.Tk()
root.title("Concurrent Web Scraper")

tk.Label(root, text="Number of pages:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Start Scraper", command=run_scraper).pack(pady=5)
tk.Button(root, text="Clear Output", command=clear_output).pack(pady=5)

output = scrolledtext.ScrolledText(root, width=60, height=20)
output.pack(pady=10)

root.mainloop()





