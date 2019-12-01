from selenium import webdriver

class BaseTest():
    driver=" "
    def __init__(self,browsername,url):
        if browsername=="Chrome":
            self.driver=webdriver.Chrome(r"C:\Users\vivek\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(url)