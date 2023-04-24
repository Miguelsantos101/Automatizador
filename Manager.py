import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
            relatorios = self.find_element(By.XPATH, "//*[@id='mat-expansion-panel-header-7']/span[1]/mat-panel-title")
            relatorios.click()

            declaracoesFechamento = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav[1]/div/app-sidebar/div/div/mat-accordion/mat-expansion-panel[6]/div/div/mat-accordion/mat-expansion-panel[7]/mat-expansion-panel-header/span/mat-panel-title")
            declaracoesFechamento.click()

            tipoRel = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/div[1]/div[2]/div/div/div/div/div/div[3]/select"))
            tipoRel.select_by_value('1')

            compIni = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/listagem-fechamento/nc-panel/fieldset/form/div[1]/div[1]/div[1]/select"))
            compIni.select_by_value('1')

            campo1 = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/listagem-fechamento/nc-panel/fieldset/form/div[1]/div[1]/div[3]/input")
            campo1.send_keys('2023')
            
            compFin = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/listagem-fechamento/nc-panel/fieldset/form/div[1]/div[2]/div[1]/select"))
            compFin.select_by_value('4')

            campo2 = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/listagem-fechamento/nc-panel/fieldset/form/div[1]/div[2]/div[3]/input")
            campo2.send_keys('2023')

            cae = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/app-declaracoes/listagem-fechamento/nc-panel/fieldset/form/div[1]/div[3]/div/input")
            cae.send_keys('0800')

            while True:
                time.sleep(600)  
        except Exception as e:
            self.error(e)
