from selenium import webdriver

driver=webdriver.Chrome(r"C:\Users\vivek\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")

signin=driver.find_element_by_id("signin_button")

signin.click()

assert "Zero - Log in" == driver.title

driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("submit").click()
driver.find_element_by_id("account_activity_tab").click()
#driver.quit()

#driver.close-it will not kill processes .it will just close current tab

#driver.quit-it will kill process.It will close all tabs

#assert keyword is for checkpoint


