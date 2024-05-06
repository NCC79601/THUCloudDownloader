import glob
from bs4 import BeautifulSoup
import downloader

def extract_tables_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        tables = soup.find_all('table')
        return tables

html_files = glob.glob('./*.html')

download_urls = []

for html_file in html_files:
    tables = extract_tables_from_html(html_file)
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            links = row.find_all('a')
            for link in links:
                href = link.get('href')
                if not href.endswith('&dl=1'):
                    continue
                download_urls.append(href)

downloader.download_urls(urls=download_urls)