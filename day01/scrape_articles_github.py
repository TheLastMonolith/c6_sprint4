from bs4 import BeautifulSoup
from IPython import embed
import requests
import time


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}

time.sleep(2)

BASE_URL ="https://albertyumol.github.io/"

def extract_html_content(target_url):
    response = requests.get(target_url, headers)
    return response.text

def main():
    """
    solution courtesy of Hurly
    """
    target_page = BASE_URL + "index.html"
    
    for x in range(1, 5):
        if x != 1:
            target_page = BASE_URL + f"page{x}/" + "index.html"
        
        html_content = extract_html_content(target_page)
        soup = BeautifulSoup(html_content, "html.parser")
        elements = soup.find_all("a", {"rel": "permalink"})
        
        for element in elements:
            print(element.get_text())

if __name__=="__main__":
    main()