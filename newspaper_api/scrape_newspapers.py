import re
import time
from pprint import pprint

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_wsj(article_url):
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')
    
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

def scrape_nyt(article_url):
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')
    div = soup.find('div', {'class': 'marginTop'})
    title_tag = div.find('title')
    
    article_title = title_tag.get_text().strip()
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
    
    print(f"Article Title: {article_title}")
    print(f"Article Time: {article_time}")
    print(f"Article Author: {article_author}")
    print(f"Article Content: {article_content}")


remove_paywall = 'https://www.RemovePaywall.com/{}'

ny_times_url = 'https://www.nytimes.com/2023/03/02/briefing/chatgpt-ai.html'
wsj_url = 'https://www.wsj.com/articles/hackathons-target-coronavirus-11586424603'

url_one = remove_paywall.format(ny_times_url)
url_two = remove_paywall.format(wsj_url)

chrome_service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless") 

browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

browser.get(url_one)
time.sleep(1)

browser.get(url_two)
scrape_nyt(ny_times_url)

