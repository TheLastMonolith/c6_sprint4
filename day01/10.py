from bs4 import BeautifulSoup
from IPython import embed
import requests
import time


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

time.sleep(2)

BASE_URL='https://albertyumol.github.io/'

def extract_html_content(target_url):
    response=requests.get(target_url, headers)
    return response.text

def main():
    target_page=BASE_URL + "index.html"
    html_content=extract_html_content(target_page)
    get_article_titles(html_content)

    for i in range(2, 5):
        html_content=extract_html_content(BASE_URL+"page"+str(i))
        get_article_titles(html_content)

def get_article_titles(content):
    soup = BeautifulSoup(content, 'html.parser')
    scraped = soup.find_all('article')

    for s in scraped:
        links = s.find_all('a')
        for link in links:
            print(link.get_text())

if __name__=="__main__":
    main()