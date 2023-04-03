import os
import time
from AutomatedWebNavigation import AutomatedWebNavigation

class Manager(AutomatedWebNavigation):
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
            os.system('cls')
            print(f'\x1b[0;31;40m {e} \x1b[0m')
            self.close()

    def navigate_to_forum(self):
        try:
            while True:
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            os.system('cls')
            print(f'\x1b[0;31;40m {e} \x1b[0m')
            self.close()
