import os
import time
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AutomatedWebNavigation(ABC):
    def __init__(self, url: str):
        self.setup(url)

    def setup(self, url: str):
        if (self.__module__ == 'src.Youtube'):
            options = webdriver.ChromeOptions() 
            options.add_argument('--user-data-dir=' + os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data')

            os.system('taskkill /f /im chrome.exe')
            os.system('taskkill /f /im chromedriver.exe')
            self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
        else:
            self.webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            
        
        self.webdriver.get(url)
        self.webdriver.set_window_position(1920, 0)
        self.webdriver.maximize_window()
        
        if (self.__module__ == 'src.Changesets' or self.__module__ == 'src.Youtube'):
            self.webdriver.implicitly_wait(5)
        else:
            self.webdriver.implicitly_wait(30)

    @abstractmethod
    def run(): pass
    
    @abstractmethod
    def navigate(): pass

    def find_element(self, by: str, value: str):
        return self.webdriver.find_element(by, value)
    
    def find_elements(self, by: str, value: str):
        return self.webdriver.find_elements(by, value)
    
    def back(self):
        return self.webdriver.back()
    
    def get(self, url: str):
        return self.webdriver.get(url)

    def error(self, exception: Exception):
        os.system('cls')
        print(f'\x1b[0;31;40m {exception} \x1b[0m')
        self.close()

    def close(self):
        if self.webdriver is not None:
            self.webdriver.quit()
