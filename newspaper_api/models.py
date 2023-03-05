from django.db import models

import re
import time
from pprint import pprint

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def get_word_classification(self):
        self.label = "Good average"
        self.text = "This is an impressive feature to add!"

    def __str__(self):
        return self.title