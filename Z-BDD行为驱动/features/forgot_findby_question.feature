Feature: forgot password find by question

	Scenario: open website
		When I open the website "https://passport.isoftstone.com/forgot"
		Then I expect that the title is "服务系统"


	Scenario: input username
		When I set with username "111"
		And I　set with code "ccc"
		And I click with nextbutton
		Then I expect that text "用户不存在"