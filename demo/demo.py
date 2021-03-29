from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://passport.isoftstone.com/forgot")
time.sleep(1)

driver.find_element_by_class_name("umobile").click()
time.sleep(1)
driver.find_element_by_name("RP_EmpDomainName").send_keys("333")
driver.find_element_by_name("RP_EmpMobile").send_keys("333")
driver.find_element_by_id("imgcode").send_keys("444")

driver.find_element_by_id("mbtn").click()
time.sleep(1)
locator = (By.XPATH, "//p[contains(text(),'验证码')]")
try:
	WebDriverWait(driver, 10,0.5).until(EC.visibility_of_element_located(locator))
	print(driver.find_element_by_xpath("//p[contains(text(),'验证码')]").text)
except:
	print("没有找到")
driver.close()