import os
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class AutomatedWebNavigation(ABC):
    def __init__(self, url: str):
        self.setup(url)

    def setup(self, url: str):
        self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.webdriver.get(url)

        self.webdriver.set_window_position(1920, 0)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(30)

    def find_element(self, by: str, value: str):
        return self.webdriver.find_element(by, value)
    
    def find_elements(self, by: str, value: str):
        return self.webdriver.find_elements(by, value)
    
    def back(self):
        return self.webdriver.back()
    
    def get(self, url: str):
        return self.webdriver.get(url)
    
    @abstractmethod
    def run(self, username, password):
        pass
    
    def error(self, exception: Exception):
        os.system('cls')
        print(f'\x1b[0;31;40m {exception} \x1b[0m')
        self.close()

    def close(self):
        if self.webdriver is not None:
            self.webdriver.quit()