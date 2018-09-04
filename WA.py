from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(executable_path = '/media/panja/New Volume/chromedriver',chrome_options=chrome_options)
driver.maximize_window()

driver.get('https://web.whatsapp.com/')

user_flag = True

while(user_flag):
	name = input("Enter the user-name :")
	search = driver.find_element_by_class_name('_2MSJr')
	search.send_keys(name)
	flag = True;
	while(flag):
		msg = input("Enter the msg :")
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()

		if(msg=='exit'):
			flag = False;
		else:
			msg_input = driver.find_element_by_class_name('_1Plpp')
			msg_input.send_keys(msg)
			button = driver.find_element_by_class_name('_35EW6')
			button.click()
	msg = input("1.user_exit 2.Continue")
	if(msg=="1"):
		user_flag = False	