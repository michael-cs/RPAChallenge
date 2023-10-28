from selenium import webdriver
from selenium.webdriver.common.by import By


def chrome_browser(site):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--enable-chrome-browser-cloud-management')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.binary_location = "C:/Users/55549/Desktop/Python/chrome-win64/chrome.exe"
    chrome_driver_path = "C:/Users/55549/Desktop/Python/chromedriver-win64/chromedriver.exe"
    service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=service_options)

    driver.get(site)

    return (driver)


class PageObjects:
    def inicia_challenge(driver):
        botao = driver.find_element(By.XPATH, "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton']")
        botao.click()

    def executa_challenge(driver, row):
        textbox = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelFirstName']")
        textbox.clear()
        textbox.send_keys(row[0])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        textbox.clear()
        textbox.send_keys(row[1])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        textbox.clear()
        textbox.send_keys(row[2])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        textbox.clear()
        textbox.send_keys(row[3])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        textbox.clear()
        textbox.send_keys(row[4])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        textbox.clear()
        textbox.send_keys(row[5])

        textbox = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        textbox.clear()
        textbox.send_keys(row[6])

        botao = driver.find_element(By.XPATH, "//input[@type='submit']")

        botao.click()

    def executa_fake_data(driver):
        first_name = driver.find_element(By.XPATH, '//div[@class="address"]/h3[1]').text.split()[0]

        last_name = driver.find_element(By.XPATH, '//div[@class="address"]/h3[1]').text.split()[-1]

        company = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[17]/dd').text

        role = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[18]/dd').text

        address = driver.find_element(By.XPATH, '//div[@class="adr"]').text.splitlines()[0]

        email = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[9]/dd[1]').text.splitlines()[0]

        phone_number = driver.find_element(By.XPATH, '//*[@id="details"]/div[2]/div[2]/div/div[2]/dl[4]/dd').text

        driver.refresh()

        return [first_name, last_name, role, company, address, email, phone_number]
