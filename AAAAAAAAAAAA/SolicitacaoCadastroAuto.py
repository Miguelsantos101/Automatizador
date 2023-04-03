from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def main():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('http://localhost:6988/SolicitacaoCadastro/TipoSolicitacaoCadastro.aspx')

    driver.set_window_position(1920, 0)
    driver.maximize_window()
    driver.implicitly_wait(1)
    action = ActionChains(driver)

    btnSaude = driver.find_element(By.XPATH, '//*[@id="btnSaude"]')
    btnSaude.click()

    txtCpfCnpj = driver.find_element('name', 'txtCpfCnpj')
    txtCpfCnpj.send_keys('13611567000146')     #txtCpfCnpj.send_keys('19.165.564/0001-02')

    # action.move_by_offset(0, 0).click().perform()

    # time.sleep(1)

    # txtEmailConfirmacao = driver.find_element('name', 'txtEmailConfirmacao')
    # txtEmailConfirmacao.send_keys('topidal874@kaftee.com')


    # txtCodAtiv = driver.find_element('name', 'txtCodAtiv')
    # txtCodAtiv.send_keys('1')
    # action.move_by_offset(0, 0).click().perform()

    # time.sleep(1)


    # txtCodAtiv2 = driver.find_element('name', 'txtCodAtiv2')
    # txtCodAtiv2.send_keys('2')
    # action.move_by_offset(0, 0).click().perform()

    # time.sleep(1)

    # txtCep = driver.find_element('name', 'txtCep')
    # txtCep.send_keys('79070140')
    # action.move_by_offset(0, 0).click().perform()

    # time.sleep(1)

    # txtNum = driver.find_element('name', 'txtNum')
    # txtNum.send_keys('123456')

    # txtFone = driver.find_element('name', 'txtFone')
    # txtFone.send_keys('999999999')

    # chkMesmoEndereco = driver.find_element('name', 'chkMesmoEndereco')
    # chkMesmoEndereco.click()


    # txtAutCpf = driver.find_element('name', 'txtAutCpf')
    # txtAutCpf.send_keys('08234775170')
    # action.move_by_offset(0, 0).click().perform()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


    # txtContCpf = driver.find_element('name', 'txtContCpf')
    # txtContCpf.send_keys('08234775170')
    # action.move_by_offset(0, 0).click().perform()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


    # txtContEmail = driver.find_element('name', 'txtContEmail')
    # txtContEmail.send_keys('topidal874@kaftee.com')

    # txtContDDD = driver.find_element('name', 'txtContDDD')
    # txtContDDD.send_keys('67')

    # txtContFone = driver.find_element('name', 'txtContFone')
    # txtContFone.send_keys('999999999')

    # driver.find_element('name', 'cbTermos').click()

    while True:
        time.sleep(1200)

if __name__ == "__main__":
    main()