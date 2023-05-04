import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from AutomatedWebNavigation import AutomatedWebNavigation

class Ava(AutomatedWebNavigation):
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
            username_element = self.find_element(By.NAME, 'username')
            username_element.send_keys(self.username)
            password_element = self.find_element(By.NAME, 'password')
            password_element.send_keys(self.password + Keys.ENTER)

            time.sleep(2)  # tempo de espera para a página carregar após o login
        except Exception as e:
            self.error(e)

    def navigate(self):
        try:
            while True:
                self.get('https://ava.ufms.br/course/view.php?id=38200')
                time.sleep(2)  # tempo de espera para a página carregar
                self.get('https://ava.ufms.br/mod/forum/view.php?id=550940')
                time.sleep(2)  # tempo de espera para a página carregar
                self.get('https://ava.ufms.br/mod/forum/discuss.php?d=115351')
                time.sleep(2)  # tempo de espera para a página carregar
                self.get('https://ava.ufms.br/course/view.php?id=38200')
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            self.error(e)
