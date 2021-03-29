from time import sleep
from behave import *
import sys
sys.path.append('..')
from lib.pages.forgot_findby_question_page import ForgotFindByQuestionPage

use_step_matcher('re')

@When('I open the website "([^"]*)"')
def step_open_website(context, url):
	ForgotFindByQuestionPage(context).get_url(url)
	#context.driver.get(url)


@Then('I expect that the title is "([^"]*)"')
def step_title(context, title_name):
	#title = context.driver.title
	title = ForgotFindByQuestionPage(context).get_title()
	print(title)
	assert title_name in title

@When('I set with username "([^"]*)"')
def step_input_username(context, username):
	ForgotFindByQuestionPage(context).send_username(username)
	#context.driver.find_element_by_id("RP_EmpDomainName").send_keys(username)

@When('I　set with code "([^"]*)"')
def step_input_code(context, code):
	ForgotFindByQuestionPage(context).send_code(code)
	#context.driver.find_element_by_id("imgcode").send_keys(code)

@When('I click with nextbutton')
def step_click_nextbutton(context):
	ForgotFindByQuestionPage(context).click_nextbutton()
	#context.driver.find_element_by_id("unext").click()

@Then('I expect that text "([^"]*)"')
def step_text(context, text1):
	text = ForgotFindByQuestionPage(context).get_text()
	#text = context.driver.find_element_by_xpath("//*[@id='prompt']/p").text
	assert text1 in text

