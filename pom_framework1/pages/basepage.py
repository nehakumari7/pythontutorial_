class Basepage:
    driver=""
    def __init__(self,d):
        self.driver=d

    def click(self,locator):
        element=self.driver.find_element(*locator)
        element.click()

    def highlight(self,element):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                   element,
                                   "border: 2px solid red;")

    def search(self,locator,text):
        self.driver.find_element(*locator).sendkeys(text)

