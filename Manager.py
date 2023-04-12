import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from AutomatedWebNavigation import AutomatedWebNavigation

class Manager(AutomatedWebNavigation):
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
            cpfcnpj = self.find_element(By.XPATH, "/html/body/app-root/div/div/mat-sidenav-container/mat-sidenav-content/div/login/div/div/div/div/div[2]/div/div/div/div/div/form/div[1]/div/input")
            cpfcnpj.send_keys(self.username)
            
            senha = self.find_element(By.XPATH, "//span[contains(text(), '-') and contains(text(), '1')]")
            senha.click()
            senha.click()
            senha.click()
            senha.click()

            submit = self.find_element(By.XPATH, "//button[@type='submit']")
            submit.click()
            
            time.sleep(2)  # tempo de espera para a página carregar após o login
        except Exception as e:
            self.error(e)

    def navigate(self):
        try:
            while True:
                time.sleep(600)  
        except Exception as e:
            self.error(e)
