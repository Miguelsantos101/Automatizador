import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:6988/SolicitacaoCadastro/TipoSolicitacaoCadastro.aspx')

    driver.set_window_position(1920, 0)
    driver.maximize_window()
    driver.implicitly_wait(1)
    action = ActionChains(driver)

    btnSaude = driver.find_element(By.XPATH, '//*[@id="btnCartao"]')
    btnSaude.click()
    
    cbLeasing = driver.find_element(By.ID, 'cbLeasing')
    cbLeasing.click()

    txtCpfCnpj = driver.find_element(By.ID, 'txtCpfCnpj')
    txtCpfCnpj.send_keys('19165564000102')     #txtCpfCnpj.send_keys('13611567000146')

    action.move_by_offset(0, 0).click().perform()

    time.sleep(1)

    txtEmailConfirmacao = driver.find_element(By.ID, 'txtEmailConfirmacao')
    txtEmailConfirmacao.send_keys('topidal874@kaftee.com')


    txtCodAtiv = driver.find_element(By.ID, 'txtCodAtiv')
    txtCodAtiv.send_keys('1')
    action.move_by_offset(0, 0).click().perform()

    time.sleep(1)


    txtCodAtiv2 = driver.find_element(By.ID, 'txtCodAtiv2')
    txtCodAtiv2.send_keys('2')
    action.move_by_offset(0, 0).click().perform()

    time.sleep(1)

    txtCep = driver.find_element(By.ID, 'txtCep')
    txtCep.send_keys('79070140')
    action.move_by_offset(0, 0).click().perform()

    time.sleep(1)

    txtNum = driver.find_element(By.ID, 'txtNum')
    txtNum.send_keys('123456')

    txtFone = driver.find_element(By.ID, 'txtFone')
    txtFone.send_keys('999999999')

    chkMesmoEndereco = driver.find_element(By.ID, 'chkMesmoEndereco')
    chkMesmoEndereco.click()


    txtAutCpf = driver.find_element(By.ID, 'txtAutCpf')
    txtAutCpf.send_keys('08234775170')
    action.move_by_offset(0, 0).click().perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


    txtContCpf = driver.find_element(By.ID, 'txtContCpf')
    txtContCpf.send_keys('08234775170')
    action.move_by_offset(0, 0).click().perform()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/button').click()


    txtContEmail = driver.find_element(By.ID, 'txtContEmail')
    txtContEmail.send_keys('topidal874@kaftee.com')

    txtContDDD = driver.find_element(By.ID, 'txtContDDD')
    txtContDDD.send_keys('67')

    txtContFone = driver.find_element(By.ID, 'txtContFone')
    txtContFone.send_keys('999999999')

    driver.find_element(By.ID, 'cbTermos').click()

    while True:
        time.sleep(1200)

if __name__ == "__main__":
    main()