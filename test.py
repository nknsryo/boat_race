# noinspection PyUnresolvedReferences
import os

from dotenv import load_dotenv

load_dotenv()
import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://kyoteibiyori.com/")
x = "出走なし"
text_2 = driver.find_element(By.XPATH, f"/html/body/div[3]/div/section[1]/div[2]/ul/li[1]").text
if x in text_2:
