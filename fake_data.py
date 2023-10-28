from navigation import ChromeBrowser, PageObjects
from file_manipulation import CriaCSVFakeData, EscreveCSVFakeData


site_data = "https://www.fakenamegenerator.com/gen-random-br-br.php"
file_path = './assets/new_challenge.csv'

driver = ChromeBrowser(site_data)

CriaCSVFakeData(file_path)

for i in range(10):
    row = (PageObjects.ExecutaFakeData(driver))
    EscreveCSVFakeData(file_path, row)
