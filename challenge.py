from navigation import chrome_browser, PageObjects
from file_manipulation import le_dados_challenge
import time

site_challenge = "https://rpachallenge.com"
driver = chrome_browser(site_challenge)
arquivo = "./assets/new_challenge.csv"

PageObjects.inicia_challenge(driver)

for i in range(10):
    row = le_dados_challenge(arquivo, i)
    PageObjects.executa_challenge(driver, row)


time.sleep(5)
