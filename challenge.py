from navigation import ChromeBrowser, PageObjects
from file_manipulation import LeDadosChallenge
import time

site_challenge = "https://rpachallenge.com"
driver = ChromeBrowser(site_challenge)
arquivo = "./assets/new_challenge.csv"

PageObjects.IniciaChallenge(driver)

for i in range(10):
    row = LeDadosChallenge(arquivo, i)
    PageObjects.ExecutaChallenge(driver, row)


time.sleep(5)
