from django.db.models.query import get_prefetcher
from selenium import webdriver
import time
driver = webdriver.Chrome()
link = "http://127.0.0.1:8000/home/"
driver.get(link)
#this waits for the new page to load
while(link == driver.current_url):
  time.sleep(1)

redirected_url = driver.current_url