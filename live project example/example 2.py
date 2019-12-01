from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(r"C:\Users\vivek\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")

signin=driver.find_element_by_id("signin_button")

signin.click()

assert "Zero - Log in" == driver.title

driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("submit").click()

driver.find_element_by_xpath('//*[@id="transfer_funds_tab"]/a').click()
fromele=driver.find_element_by_css_selector("#tf_fromAccountId")
fromacnt=Select(fromele)
fromacnt.select_by_index(3)
fromacnt.select_by_value("3")
fromacnt.select_by_visible_text("Savings(Avail. balance = $ 1000)")

toele=driver.find_element_by_xpath('//*[@id="tf_toAccountId"]')
toacnt=Select(toele)
toacnt.select_by_visible_text("Checking(Avail. balance = $ -500.2)")
driver.find_element_by_css_selector("#tf_amount").send_keys("100")
driver.find_element_by_css_selector("#tf_description").send_keys("payment")
driver.find_element_by_css_selector("#btn_submit").click()

fromele=driver.find_element_by_css_selector("#tf_fromAccountId")
assert False==fromele.is_enabled()



toele=driver.find_element_by_css_selector("#tf_toAccountId")

assert False==toele.is_enabled()

amontt=driver.find_element_by_css_selector("#tf_amount")
assert False==amontt.is_enabled()

descp=driver.find_element_by_css_selector("#tf_description")

assert False==descp.is_enabled()

driver.find_element_by_css_selector("#btn_submit").click()


confirmmsg=driver.find_element_by_css_selector("#transfer_funds_content > div > div > div.alert.alert-success").text

assert "You successfully submitted your transaction." in confirmmsg
