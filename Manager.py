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

            time.sleep(1)

            fiscalizacao = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav[1]/div/app-sidebar/div/div/mat-accordion/mat-expansion-panel[6]/div/div/mat-accordion/mat-expansion-panel[11]/mat-expansion-panel-header/span/mat-panel-title")
            fiscalizacao.click()

            time.sleep(1)

            tipoRel = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/div/div[2]/div/div/div/div/div/div[2]/div[2]/select"))
            tipoRel.select_by_value('6')

            periodoIni = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/rel-de-correspondencia/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/input")
            periodoIni.send_keys('11')
            periodoIni.send_keys('04')
            periodoIni.send_keys('2023')

            periodoFin = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/rel-de-correspondencia/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[3]/div/input")
            periodoFin.send_keys('12')
            periodoFin.send_keys('04')
            periodoFin.send_keys('2023')
            
            InscricaoMunicipal = self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/rel-de-correspondencia/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/input")
            InscricaoMunicipal.send_keys('022')
            
            tipoFiscal = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/rel-de-correspondencia/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/select"))
            tipoFiscal.select_by_visible_text('Miguel dos Santos Flores')
            
            tipoNatureza = Select(self.find_element(By.XPATH, "/html/body/app-root/div/div[2]/mat-sidenav-container/mat-sidenav-content/div/rel-fiscalizacao/rel-de-correspondencia/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[3]/select"))
            tipoNatureza.select_by_value('3')
            while True:
                time.sleep(600)  
        except Exception as e:
            self.error(e)
