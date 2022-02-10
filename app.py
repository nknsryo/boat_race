# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys
# noinspection PyUnresolvedReferences
import csv
# noinspection PyUnresolvedReferences
import psycopg2 as psycopg2
# noinspection PyUnresolvedReferences
from dotenv import load_dotenv
from scraping import get_scraping_data
from db_ import init_db

load_dotenv()


def main():
    init_db.init_db()
    get_scraping_data.get_scraping_data()


if __name__ == "__main__":
    main()
