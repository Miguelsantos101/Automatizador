import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from AutomatedWebNavigation import AutomatedWebNavigation

class Online(AutomatedWebNavigation):
    def __init__(self, url: str, username: str, password: str):
        super().__init__(url)
        self.username = username
        self.password = password
        self.run()

    def run(self):
        self.login()
        self.navigate()

    def login(self):
        try:
            cpfcnpj = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/input")
            cpfcnpj.send_keys(self.username)
            
            senha = self.find_element(By.XPATH, "//input[contains(@value, '1') and contains(@value, '-')]")
            senha.click()
            senha.click()
            senha.click()
            senha.click()
            
            submit = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/input")
            submit.click()
        except Exception as e:
            self.error(e)

    def navigate(self):
        try:
            cae = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/input")
            cae.send_keys('0800')
            
            pesquisarCae = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[6]/a")
            pesquisarCae.click()
            
            btnMenus = self.find_element(By.XPATH, "/html/body/form/div[1]/div/a")
            btnMenus.click()
            
            while True:
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            self.error(e)
