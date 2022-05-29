from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class VagasAuto:
    def __init__(self):
        self.caminho_driver= "chromedriver"
        self.chrome= webdriver.Chrome(
            self.caminho_driver
        )

    def acessar_site(self,site):
        self.chrome.get(site)

    def quit_site(self):
        self.chrome.quit()

    def acessar_singin(self):
        entra= self.chrome.find_element(By.XPATH,'/html/body/nav/div/a[2]')
        entra.click()
    
    def logon(self, login, senha):
        check_login= self.chrome.find_element(By.XPATH, '//*[@id="username"]')
        check_login.send_keys(login)
        check_password= self.chrome.find_element(By.XPATH, '//*[@id="password"]')
        check_password.send_keys(senha)

        get_login= self.chrome.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
        get_login.click()

    def check_logon(self):
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="ember17"]').click()
            
            
        except:
            self.logon("Your email","Your password")
    
    def procurar_vaga(self):
        self.chrome.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input').send_keys("Engenharia de Software", Keys.ENTER)
        sleep(3)
        self.chrome.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()
        
       

       

if __name__ == "__main__":
    chrome= VagasAuto()
    chrome.acessar_site("http://linkedin.com/home")
    sleep(3)
    chrome.acessar_singin()
    sleep(2)
    chrome.check_logon()
    sleep(3)

    chrome.procurar_vaga()
    sleep(3)
    chrome.quit_site()