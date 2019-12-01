from selenium.webdriver.common.by import By
from pom_framework1.pages.basepage import Basepage

class HomePage(Basepage):


    sign_in_button=By.ID,"signin_button"
    search_button=By.ID,"searchTerm"

    def click_signin(self):
        self.click(self.sign_in_button)

    def search(self,text):
        self.search(self.search_button,text)

