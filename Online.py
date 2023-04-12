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
        self.navigate_to_forum()

    def login(self):
        try:


            time.sleep(2)  # tempo de espera para a página carregar após o login
        except Exception as e:
            self.error(e)

    def navigate_to_forum(self):
        try:
            while True:
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            self.error(e)
