
import os
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AutomatedWebNavigation(ABC):
    def __init__(self, url: str):
        self.setup(url)

    def setup(self, url: str):
        self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.webdriver.get(url)

        self.webdriver.set_window_position(1920, 0)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(1)

    def find_element(self, by: str, value: str):
        return self.webdriver.find_element(by, value)
    
    @abstractmethod
    def run(self, username, password):
        pass

    def close(self):
        if self.webdriver is not None:
            self.webdriver.quit()
    
    def error(self, exception: Exception):
        os.system('cls')
        print(f'\x1b[0;31;40m {exception} \x1b[0m')
        self.close()