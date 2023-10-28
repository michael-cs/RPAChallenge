from navigation import chrome_browser, PageObjects
from file_manipulation import cria_csv, escreve_csv


site_data = "https://www.fakenamegenerator.com/gen-random-br-br.php"
file_path = './assets/new_challenge.csv'

driver = chrome_browser(site_data)

cria_csv(file_path)

for i in range(10):
    row = (PageObjects.executa_fake_data(driver))
    escreve_csv(file_path, row)
