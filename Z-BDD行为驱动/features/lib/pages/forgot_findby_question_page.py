import sys

sys.path.append('../..')
from lib.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ForgotFindByQuestionPage(BasePage):
	def __init__(self, context):
		super(ForgotFindByQuestionPage, self).__init__(context.driver)

	def send_username(self, username):
		self.find_element(By.ID,'RP_EmpDomainName').send_keys(username)

	def send_code(self, code):
		self.find_element(By.ID, 'imgcode').send_keys(code)

	def click_nextbutton(self):
		self.find_element(By.ID, 'unext').click()

	def get_text(self):
		locator = (By.XPATH, "//*[@id='prompt']/p")
		try:
			WebDriverWait(self.driver, 30,0.5).until(EC.visibility_of_element_located(locator))
			return self.find_element(By.XPATH, "//*[@id='prompt']/p").text
		except Exception as e:
			return None
if __name__ == '__main__':
	print(sys.path)




