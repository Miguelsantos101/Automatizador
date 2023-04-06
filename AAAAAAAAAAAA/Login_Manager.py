import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def main():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('http://localhost:4200/login')

        driver.set_window_position(1920, 0)
        driver.maximize_window()
        driver.implicitly_wait(30)

        cpfcnpj = driver.find_element(By.XPATH, "//input[@inputid='cpfcnpj']")
        cpfcnpj.send_keys('08234775170')

        senha = driver.find_element(By.XPATH, "//span[contains(text(), '-') and contains(text(), '1')]")
        senha.click()
        senha.click()
        senha.click()
        senha.click()

        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit.click()

        time.sleep(1)

        relatorios = driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-7']/span[1]/mat-panel-title")
        relatorios.click()

        time.sleep(1)

        desif = driver.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-57']/span/mat-panel-title")
        desif.click()

        time.sleep(1)

        tipoRel = Select(driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-desif/div/div[2]/div/div/div/div[3]/select"))
        tipoRel.select_by_value('2')

        inscricaoMunicipal = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-desif/app-declaracao-desif/div/div[2]/form/div/div/div/div[1]/div/div/input")
        inscricaoMunicipal.send_keys('152')

        while True:
            time.sleep(1200)
            
    except Exception as e:
        os.system('cls')
        print(f'\x1b[0;31;40m {e} \x1b[0m')
    finally:
        quit()

if __name__ == "__main__":
    main()