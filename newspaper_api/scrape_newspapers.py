import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from newspaper_api.models import Newspaper

def scrape_wsj(url):
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get(url)
    time.sleep(1)

    src = browser.page_source
    soup = BeautifulSoup(src, 'html.parser')
    
    article_title = soup.title.get_text()
    article_content = ""
    article_time = None
    article_author = None
    
    article_content_div = soup.find('div', {'class': 'article-content'})
    p_tags = article_content_div.find_all('p')
    
    for p_tag in p_tags:
        paragraph = p_tag.get_text().strip()
        article_content += paragraph
        
    author = soup.find('meta', {'name': 'author'})
    if author:
        article_author = author['content']
        
    article_time_elem = soup.find('time', {'class': 'timestamp article__timestamp flexbox__flex--1'})
    if article_time_elem:
        article_time = article_time_elem.get_text().strip()

    newspaper = Newspaper.objects.create(title=article_title, author=article_author, content=article_content, pub_date=article_time)

    browser.quit()
    
    return newspaper


def scrape_nyt(url):
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get(url)
    time.sleep(1)

    src = browser.page_source
    soup = BeautifulSoup(src, 'html.parser')
    
    article_title = soup.title.get_text().strip()
    article_content = ""
    article_time = None   
    article_author = None
    
    divs = soup.find_all('div', {'class': 'StoryBodyCompanionColumn'})
    for div in divs:
        p_tags = div.find_all('p')

        for p_tag in p_tags:
            paragraph = p_tag.get_text().strip()
            article_content += paragraph
        
    article_author = soup.find('meta', {'name': 'byl'})['content'].split()[-1].strip()
        
    meta_published_tag = soup.find('meta', {'property': 'article:published_time'})
    article_time = meta_published_tag['content']
    
    newspaper = Newspaper.objects.create(title=article_title, author=article_author, content=article_content, pub_date=article_time)

    browser.quit()
    
    return newspaper
