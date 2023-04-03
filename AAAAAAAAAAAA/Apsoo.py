import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main ():
    try:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://ava.ufms.br/login/index.php')

        driver.set_window_position(1920, 0)
        driver.maximize_window()
        driver.implicitly_wait(1)

        username = driver.find_element('name', 'username')
        username.send_keys('miguel.s')
        password = driver.find_element('name', 'password')
        password.send_keys('miguelsantosMM26*' + Keys.ENTER)

        while True:
            time.sleep(2)
            driver.get('https://ava.ufms.br/course/view.php?id=38200')
            time.sleep(2)
            driver.get('https://ava.ufms.br/mod/forum/view.php?id=550940')
            time.sleep(2)
            driver.get('https://ava.ufms.br/mod/forum/discuss.php?d=115351')
            time.sleep(2)
            driver.get('https://ava.ufms.br/course/view.php?id=38200')
            time.sleep(600)
    except Exception as e:
        os.system('cls')
        print(f'\x1b[0;31;40m {e} \x1b[0m')
    finally:
        quit()
    
if __name__ == "__main__":
    main()