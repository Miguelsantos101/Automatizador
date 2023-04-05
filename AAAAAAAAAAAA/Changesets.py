import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://nccgtfs01:8080/tfs/NotaControl/ISS%20ONLINE/_backlogs/TaskBoard/Online%20ISS%20Vers%C3%A3o%20-%20Abril%202023/Licita%C3%A7%C3%A3o%20Contagem%201.3?_a=requirements')

    driver.set_window_position(1920, 0)
    driver.maximize_window()
    driver.implicitly_wait(1)

    expand_collapse_button = driver.find_element(By.ID, 'expand-collapse-button')
    expand_collapse_button.click()
    expand_collapse_button.click()

    task = driver.find_elements(By.XPATH, "//div[@aria-roledescription='Card' and descendant::div[contains(text(), 'Development')]]//span[@class='clickable-title']")
    lista_de_changesets = []
    for i in range(len(task)):
        task_atual = task[i]
        task_atual.click()
        time.sleep(1)
        changesets = task[i].find_elements(By.XPATH, "//*[starts-with(@class, 'links-control-container')]//*[text() [contains(., 'Changeset')]]")
        if len(changesets) == 0:
            pass
        else:
            for i in range(len(changesets)):
                lista_de_changesets.append(changesets[i].text)
        driver.back()
        time.sleep(1)

    nome_arquivo = 'Changesets.txt'
    lista_de_changesets = remover_parte_especifica(lista_de_changesets, 'Changeset ')
    lista_de_changesets.sort()

    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
    
    escrever_strings_em_arquivo(lista_de_changesets, nome_arquivo)
    os.system(nome_arquivo)

def remover_parte_especifica(strings, parte):
    resultado = [s.replace(parte, '') for s in strings]
    return resultado


def escrever_strings_em_arquivo(strings, nome_arquivo):
    # Obtem o caminho absoluto do diretório do programa
    diretorio_programa = os.path.abspath(os.path.dirname(__file__))
    # Junta o nome do arquivo ao caminho absoluto do diretório
    caminho_arquivo = os.path.join(diretorio_programa, nome_arquivo)

    # Abre o arquivo no modo de escrita
    with open(caminho_arquivo, 'w') as arquivo:
        # Percorre a lista de strings
        for s in strings:
            # Escreve a string no arquivo, seguida de uma quebra de linha
            arquivo.write(s + '\n')


if __name__ == "__main__":
    main()