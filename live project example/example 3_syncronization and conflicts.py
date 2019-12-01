from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#try:

driver=webdriver.Chrome(r"C:\Users\vivek\Desktop\Selenium\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("http://zero.webappsecurity.com")

signin=driver.find_element_by_id("signin_button")

signin.click()

assert "Zero - Log in" == driver.title

driver.find_element_by_id("user_login").send_keys("username")
driver.find_element_by_id("user_password").send_keys("password")
driver.find_element_by_name("submit").click()
driver.find_element_by_xpath("//a[contains(text(),'Pay Bills')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Purchase Foreign Currency')]").click()

#time.sleep(3)
driver.implicitly_wait(3)
#implicit will wait for 3 sec for all find by eement case-this is conditional wait
#time.sleep is unconditional wait
# by defalut polling timme in chrome and mozilla is 5ms
#implicit wait is not recommended in practice as it will wait for all the find elements.it is decalred globally
wait=WebDriverWait(driver,3)
currencyele=wait.until(EC.visibility_of_element_located((By.ID,"pc_currency")))
curreny=Select(currencyele)
curreny.select_by_visible_text("Switzerland (franc)")
#driver.find_element_by_id("pc_currency").send_keys("Switzerland (franc")
sellrate=wait.until(EC.visibility_of_element_located((By.ID,"sp_sell_rate")))
sellratevalue=sellrate.text.split(' ')[4]
#print(sellratevalue)
driver.find_element_by_id("pc_amount").send_keys("100")
selectedcurren=driver.find_element_by_id("pc_inDollars_false")
if selectedcurren.is_selected()==False :
    selectedcurren.click()

driver.find_element_by_id("pc_calculate_costs").click()
actualvalue=wait.until(EC.visibility_of_element_located((By.ID,"pc_conversion_amount")))
actual_amount=actualvalue.text.split(' ')[4]
print(actual_amount)
