# WebPathScraper
A Python-based tool that extracts all website paths from a given URL and downloads relevant files such as PDFs and images. It utilizes BeautifulSoup for web scraping and automates file retrieval.
WebPathScraper
Overview
WebPathScraper is a Python-based tool that extracts all website paths from a given URL and downloads relevant files such as PDFs and images. It utilizes BeautifulSoup for web scraping and automates file retrieval.

Features
Extracts all links from a website

Downloads PDF and image files automatically

Handles errors gracefully

Allows users to specify a save directory for downloaded files

Prerequisites
Ensure you have Python installed (Python 3 recommended). You also need to install the required dependencies:

pip install requests beautifulsoup4
Installation
Clone the repository and navigate to the project directory:

git clone https://github.com/yourusername/WebPathScraper.git
cd WebPathScraper
Usage
Run the script and provide a website URL and a directory to save the downloaded files:

python amr&mosa.py
Follow the prompts to enter the URL and destination folder.

Example
Enter website URL: https://example.com
Paths found:
https://example.com/file1.pdf
https://example.com/image1.jpg
Enter directory to save files: /downloads
Downloading file1.pdf...
Downloading image1.jpg...
Download complete.
Technologies Used
Python

Requests

BeautifulSoup (bs4)

OS module

Contributing
Feel free to fork this repository and submit pull requests.

License
This project is licensed under the MIT License
