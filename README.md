# 🌐 Automatic Web Scraper

A **Python-based web scraper** that fetches and parses **HTML pages from multiple domains** using **asynchronous techniques**. Built with **asyncio**, **aiohttp**, and **BeautifulSoup**, this scraper efficiently handles network I/O and fetches pages concurrently.

---

## 🚀 Features

- **Two Versions Available:**
  1. **Version 1 – Dummy Data:**  
     - Uses pre-defined or dummy URLs for **fast testing**.  
     - Perfect for quick validation of scraper functionality.  
  2. **Version 2 – Real-Time Web Pages:**  
     - Automatically crawls **real websites** starting from seed URLs.  
     - Fetches live content from multiple domains.  
     - Slower due to network I/O and real-world site delays, but **produces actual web data**.

- **Concurrent Fetching:** `aiohttp` + `asyncio` for efficient non-blocking network requests.  
- **User-Friendly UI:** Tkinter-based interface for real-time status and output.  
- **Customizable:** Input number of pages to fetch and starting seed URLs.  
- **Unique Domains:** Ensures fetched pages are from different domains.  
- **Real-Time Output:** Shows fetched URLs and page titles dynamically.

---

## 💻 Technologies Used

- **Python 3.8+**  
- **aiohttp** → Asynchronous HTTP requests  
- **asyncio** → Concurrency handling  
- **BeautifulSoup4** → HTML parsing  
- **Tkinter** → Graphical User Interface  

---

## 🎯 How It Works

1. Choose **Version 1** for fast dummy testing or **Version 2** for real-time fetching.  
2. For Version 2, enter **seed URLs** and **number of pages** in the UI.  
3. Click **Start Scraper**:  
    - Scraper fetches pages concurrently.  
    - Extracts page titles and discovers new links automatically (Version 2).  
4. Output shows all fetched pages and **total unique domains** at the end.

---

## Install dependencies:

pip install aiohttp beautifulsoup4

---

## Run the scraper:

# Version 1 – Dummy data
python app.py

# Version 2 – Real-time web pages
python main.py

---

## 🎨 Screenshots

Real-time output showing fetched pages and page titles.

## 🛠 Usage Tips

Version 1 is fast; ideal for testing and development.

Version 2 fetches live web pages; may take longer depending on network and website responsiveness.

Avoid JS-heavy or login-protected websites for Version 2.

## 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

## ⭐ Feedback

If you enjoy using this scraper, give it a star 🌟 and share your feedback!

If you want, I can **also add a table in the README comparing Version 1 and Version 2** side by side, which looks more **professional and visually clear** for GitHub viewers.  

---

