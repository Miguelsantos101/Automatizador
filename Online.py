import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from AutomatedWebNavigation import AutomatedWebNavigation

class Online(AutomatedWebNavigation):
    def __init__(self, url: str, username: str, password: str, mode: int = 0):
        super().__init__(url)
        self.username = username
        self.password = password
        self.mode = mode
        self.run()

    def run(self):
        if (self.mode == 1):
            self.solCadAuto()
        else:
            self.login()
            self.navigate()

    def login(self):
        try:
            cpfcnpj = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/input")
            cpfcnpj.send_keys(self.username)
            
            senha = self.find_element(By.XPATH, "//input[contains(@value, '1') and contains(@value, '-')]")
            senha.click()
            senha.click()
            senha.click()
            senha.click()
            
            submit = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/input")
            submit.click()
        except Exception as e:
            self.error(e)

    def navigate(self):
        try:
            cae = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/input")
            cae.send_keys('0800')
            
            pesquisarCae = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[6]/a")
            pesquisarCae.click()
            
            btnMenus = self.find_element(By.XPATH, "/html/body/form/div[1]/div/a")
            btnMenus.click()
            
            while True:
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            self.error(e)

    def solCadAuto(self):
        try:
            action = ActionChains(self.webdriver)
            solCadLink = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[1]/div[4]/ul/li[1]/a/span")
            solCadLink.click()
            
            cardAvulso = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/a")
            cardAvulso.click()
            
            rbPessoaJuridica = self.find_element(By.ID, 'rbPessoaJuridica')
            rbPessoaJuridica.click()

            txtCpfCnpj = self.find_element(By.ID, 'txtCpfCnpj')
            txtCpfCnpj.send_keys('19165564000102')     #txtCpfCnpj.send_keys('13611567000146')

            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtEmailConfirmacao = self.find_element(By.ID, 'txtEmailConfirmacao')
            txtEmailConfirmacao.send_keys('topidal874@kaftee.com')


            txtCodAtiv = self.find_element(By.ID, 'txtCodAtiv')
            txtCodAtiv.send_keys('2')
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)


            txtCodAtiv2 = self.find_element(By.ID, 'txtCodAtiv2')
            txtCodAtiv2.send_keys('3')
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtCep = self.find_element(By.ID, 'txtCep')
            txtCep.send_keys('79070140')
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtNum = self.find_element(By.ID, 'txtNum')
            txtNum.send_keys('123456')

            txtFone = self.find_element(By.ID, 'txtFone')
            txtFone.send_keys('999999999')

            chkMesmoEndereco = self.find_element(By.ID, 'chkMesmoEndereco')
            chkMesmoEndereco.click()


            txtAutCpf = self.find_element(By.ID, 'txtAutCpf')
            txtAutCpf.send_keys('08234775170')
            action.move_by_offset(0, 0).click().perform()
            time.sleep(2)
            self.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


            txtContCpf = self.find_element(By.ID, 'txtContCpf')
            txtContCpf.send_keys('08234775170')
            action.move_by_offset(0, 0).click().perform()
            time.sleep(2)
            self.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


            txtContEmail = self.find_element(By.ID, 'txtContEmail')
            txtContEmail.send_keys('topidal874@kaftee.com')

            txtContDDD = self.find_element(By.ID, 'txtContDDD')
            txtContDDD.send_keys('67')

            txtContFone = self.find_element(By.ID, 'txtContFone')
            txtContFone.send_keys('999999999')

            self.find_element(By.ID, 'cbTermos').click()
            
            while True:
                time.sleep(600)  # tempo de espera de 10 minutos
        except Exception as e:
            self.error(e)