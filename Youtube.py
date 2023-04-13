from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from AutomatedWebNavigation import AutomatedWebNavigation

class Youtube(AutomatedWebNavigation):
    def __init__(self, url: str):
        super().__init__(url)
        self.url = url
        self.run()

    def run(self):
        self.navigate()

    def navigate(self):
        try:
            while True:
                inscricoes = self.find_elements(By.XPATH, "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]//ytd-guide-entry-renderer[@line-end-style='dot']")
                if inscricoes.__len__() > 0:
                    for canal in inscricoes:
                        canal.click()
                        self.back()
                    self.get(self.url)
                else:
                    self.close()
                    break

        except Exception as e:
            self.error(e)


