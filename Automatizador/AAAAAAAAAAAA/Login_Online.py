import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:6988/Login/Login.aspx')

    driver.set_window_position(1920, 0)
    driver.maximize_window()
    driver.implicitly_wait(1)

    txtLogin = driver.find_element('name', 'txtLogin')
    txtLogin.send_keys('08234775170')

    senha = driver.find_element(By.XPATH, "//input[starts-with(@value, '') and contains(@value, '-') and contains(@value, '1')]")
    senha.click()
    senha.click()
    senha.click()
    senha.click()

    btnAcessar = driver.find_element(By.XPATH, '//*[@id="btnAcessar"]')
    btnAcessar.click()

    time.sleep(1)

    txtCae = driver.find_element(By.XPATH, '//*[@id="txtCae"]')
    txtCae.send_keys('0800' + Keys.ENTER)

    time.sleep(1)

    menu_toggle = driver.find_element(By.XPATH, '//*[@id="menu-toggle"]')
    menu_toggle.click()

    while True:
        time.sleep(1200)


if __name__ == "__main__":
    main()