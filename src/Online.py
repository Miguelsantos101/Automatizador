import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from src.AutomatedWebNavigation import AutomatedWebNavigation


class Online(AutomatedWebNavigation):
    def __init__(self, url: str, username: str, password: str, mode: int = 0):
        super().__init__(url)
        self.username = username
        self.password = password
        self.mode = mode
        self.run()

    def run(self):
        if self.mode == 1:
            self.solCadAuto()
        else:
            self.login()
            self.navigate()

    def login(self):
        try:
            cpfcnpj = self.find_element(
                By.XPATH,
                "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/input",
            )
            cpfcnpj.send_keys(self.username)

            senha = self.find_element(
                By.XPATH, "//input[contains(@value, '1') and contains(@value, '-')]"
            )
            senha.click()
            senha.click()
            senha.click()
            senha.click()

            submit = self.find_element(
                By.XPATH,
                "/html/body/form/div/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/input",
            )
            submit.click()
        except Exception as e:
            self.error(e)

    def navigate(self):
        try:
            cae = self.find_element(
                By.XPATH,
                "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/input",
            )
            cae.send_keys("0800")

            pesquisarCae = self.find_element(
                By.XPATH,
                "/html/body/form/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div[6]/a",
            )
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
            solCadLink = self.find_element(
                By.XPATH,
                "/html/body/form/div/div[1]/div/div/div/div/div[1]/div[4]/ul/li[1]/a/span",
            )
            solCadLink.click()

            cardAvulso = self.find_element(
                By.XPATH,
                "/html/body/form/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[2]/a",
            )
            cardAvulso.click()

            txtCpfCnpj = self.find_element(By.ID, "txtCpfCnpj")
            txtCpfCnpj.send_keys(
                "94726945000139"
            )  # txtCpfCnpj.send_keys('13611567000146')

            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtNomeRazao = self.find_element(By.ID, "txtNome")
            txtNomeRazao.send_keys("Task de Correção")

            txtNomeFantasia = self.find_element(By.ID, "txtNomeFantasia")
            txtNomeFantasia.send_keys("Task de Correção")

            txtEmail = self.find_element(By.ID, "txtEmail")
            txtEmail.send_keys("teste@teste.com")

            txtEmailConfirmacao = self.find_element(By.ID, "txtEmailConfirmacao")
            txtEmailConfirmacao.send_keys("teste@teste.com")

            txtCodAtiv = self.find_element(By.ID, "txtCodAtiv")
            txtCodAtiv.send_keys("6")
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtCodAtiv2 = self.find_element(By.ID, "txtCodAtiv2")
            txtCodAtiv2.send_keys("7")
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtCep = self.find_element(By.ID, "txtCep")
            txtCep.send_keys("79008070")
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtNum = self.find_element(By.ID, "txtNum")
            txtNum.send_keys("29")

            txtDDD = self.find_element(By.ID, "txtDDD")
            txtDDD.send_keys("67")

            txtFone = self.find_element(By.ID, "txtFone")
            txtFone.send_keys("999999999")

            txtDDDFax = self.find_element(By.ID, "txtDDDFax")
            txtDDDFax.send_keys("67")

            txtCorCep = self.find_element(By.ID, "txtCorCep")
            txtCorCep.send_keys("79008070")
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            txtCorNum = self.find_element(By.ID, "txtCorNum")
            txtCorNum.send_keys("29")

            txtCorDDD = self.find_element(By.ID, "txtCorDDD")
            txtCorDDD.send_keys("67")

            txtCorFone = self.find_element(By.ID, "txtCorFone")
            txtCorFone.send_keys("999999999")

            txtCorDDDFax = self.find_element(By.ID, "txtCorDDDFax")
            txtCorDDDFax.send_keys("67")

            txtAutCpf = self.find_element(By.ID, "txtAutCpf")
            txtAutCpf.send_keys("73621017321")
            action.move_by_offset(0, 0).click().perform()
            time.sleep(2)

            txtAutNome = self.find_element(By.ID, "txtAutNome")
            txtAutNome.send_keys("Antonio")

            txtContCpf = self.find_element(By.ID, "txtContCpf")
            txtContCpf.send_keys("64246759228")
            action.move_by_offset(0, 0).click().perform()
            time.sleep(2)
            self.find_element(
                By.XPATH, "/html/body/div[1]/div/div/div[3]/div/button"
            ).click()

            txtContCep = self.find_element(By.ID, "txtContCep")
            txtContCep.send_keys("95270000")
            action.move_by_offset(0, 0).click().perform()

            time.sleep(1)

            iframeModal = self.find_element(By.ID, "iframeModal")
            self.webdriver.switch_to.frame(iframeModal)
            self.find_element(
                By.XPATH, '//*[@id="dgLogradouros__ctl6_ibtSeleciona"]'
            ).click()
            self.webdriver.switch_to.default_content()

            self.webdriver.execute_script("window.scrollTo(0, 500);")

            cbTermos = self.find_element(By.ID, "cbTermos")
            cbTermos.click()

            while True:
                time.sleep(600)
        except Exception as e:
            self.error(e)

        # AVULSO

        # try:
        #     action = ActionChains(self.webdriver)
        #     solCadLink = self.find_element(By.XPATH, "/html/body/form/div/div[1]/div/div/div/div/div[1]/div[4]/ul/li[1]/a/span")
        #     solCadLink.click()

        #     cardAvulso = self.find_element(By.XPATH, "/html/body/form/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div[1]/a")
        #     cardAvulso.click()

        #     rbPessoaJuridica = self.find_element(By.ID, 'rbPessoaJuridica')
        #     rbPessoaJuridica.click()

        #     txtCpfCnpj = self.find_element(By.ID, 'txtCpfCnpj')
        #     txtCpfCnpj.send_keys('19165564000102')     #txtCpfCnpj.send_keys('13611567000146')

        #     action.move_by_offset(0, 0).click().perform()

        #     time.sleep(1)

        #     txtEmailConfirmacao = self.find_element(By.ID, 'txtEmailConfirmacao')
        #     txtEmailConfirmacao.send_keys('topidal874@kaftee.com')

        #     txtCodAtiv = self.find_element(By.ID, 'txtCodAtiv')
        #     txtCodAtiv.send_keys('2')
        #     action.move_by_offset(0, 0).click().perform()

        #     time.sleep(1)

        #     txtCodAtiv2 = self.find_element(By.ID, 'txtCodAtiv2')
        #     txtCodAtiv2.send_keys('3')
        #     action.move_by_offset(0, 0).click().perform()

        #     time.sleep(1)

        #     txtCep = self.find_element(By.ID, 'txtCep')
        #     txtCep.send_keys('79070140')
        #     action.move_by_offset(0, 0).click().perform()

        #     time.sleep(1)

        #     txtNum = self.find_element(By.ID, 'txtNum')
        #     txtNum.send_keys('123456')

        #     txtFone = self.find_element(By.ID, 'txtFone')
        #     txtFone.send_keys('999999999')

        #     chkMesmoEndereco = self.find_element(By.ID, 'chkMesmoEndereco')
        #     chkMesmoEndereco.click()

        #     txtAutCpf = self.find_element(By.ID, 'txtAutCpf')
        #     txtAutCpf.send_keys('08234775170')
        #     action.move_by_offset(0, 0).click().perform()
        #     time.sleep(2)
        #     self.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()

        #     txtContCpf = self.find_element(By.ID, 'txtContCpf')
        #     txtContCpf.send_keys('08234775170')
        #     action.move_by_offset(0, 0).click().perform()
        #     time.sleep(2)
        #     self.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()

        #     txtContEmail = self.find_element(By.ID, 'txtContEmail')
        #     txtContEmail.send_keys('topidal874@kaftee.com')

        #     txtContDDD = self.find_element(By.ID, 'txtContDDD')
        #     txtContDDD.send_keys('67')

        #     txtContFone = self.find_element(By.ID, 'txtContFone')
        #     txtContFone.send_keys('999999999')

        #     self.find_element(By.ID, 'cbTermos').click()

        #     while True:
        #         time.sleep(600)
        # except Exception as e:
        #     self.error(e)
