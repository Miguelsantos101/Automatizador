import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from AutomatedWebNavigation import AutomatedWebNavigation

class Changesets(AutomatedWebNavigation):
    def __init__(self, url: str, doSort: bool = True):
        super().__init__(url)
        self.doSort = doSort
        self.run()

    def run(self):
        self.navigate()

    def navigate(self):
        try:
            expand_collapse_button = self.find_element(By.ID, 'expand-collapse-button')
            expand_collapse_button.click()
            expand_collapse_button.click()

            task = self.find_elements(By.XPATH, "//div[@aria-roledescription='Card' and descendant::div[contains(text(), 'Development')]]//span[@class='clickable-title']")
            lista_de_changesets = []
            
            for i in range(len(task)):
                task_atual = task[i]
                task_atual.click()
                changesets = task[i].find_elements(By.XPATH, "//*[starts-with(@class, 'links-control-container')]//*[text() [contains(., 'Changeset')]]")
                
                if len(changesets) == 0:
                    pass
                else:
                    while True:
                        procuraShowmore = task[i].find_elements(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div")
                        if (len(procuraShowmore) > 1):
                            botaoShowmore = procuraShowmore[1].find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]")
                            botaoShowmore.click()
                            changesets = task[i].find_elements(By.XPATH, "//*[starts-with(@class, 'links-control-container')]//*[text() [contains(., 'Changeset')]]")
                        else:
                            break
                    
                    self.adiciona_changesets(lista_de_changesets, changesets)

                self.back()
                
            nome_arquivo = 'Changesets.txt'
            lista_de_changesets = self.remover_parte_especifica(lista_de_changesets, 'Changeset ')
            
            if (self.doSort):
                lista_de_changesets.sort()

            if os.path.exists(nome_arquivo):
                os.remove(nome_arquivo)
            
            self.escrever_strings_em_arquivo(lista_de_changesets, nome_arquivo)
            os.system(nome_arquivo)

        except Exception as e:
            self.error(e)
            
    def adiciona_changesets(self, lista_de_changesets, changesets):
        for i in range(len(changesets)):
            lista_de_changesets.append(changesets[i].text)
    
    def remover_parte_especifica(self, strings, parte):
        resultado = [s.replace(parte, '') for s in strings]
        return resultado

    def escrever_strings_em_arquivo(self, strings, nome_arquivo):
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
