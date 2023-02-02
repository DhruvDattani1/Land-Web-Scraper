from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

Name = []
RD = []
Designer = []
CW = []
driver.get('https://www.goat.com/sneakers/wmns-air-jordan-1-mid-stealth-bq6472-115')
info = driver.page_source
soup = BeautifulSoup(info, features='html')