import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\hack\\chromedriver.exe")
url= "https://wn7pokerdom.com/auth/login"

# try:
driver.get(url=url)
# driver.get(url="gmail.com")    
# time.sleep(5)
nik = "mhv@ggr.group"
passwd = '11111111'
nik_xpath = '/html/body/pd-root/div/div/ng-component/main/section/ng-component/ng-component/form/section/pd-input-login/section/div/input'
driver.find_elements_by_xpath(nik_xpath).send_keys("nik")

passwd_xpath = '/html/body/pd-root/div/div/ng-component/main/section/ng-component/ng-component/form/section/pd-input-password/section/div/input'
driver.find_elements_by_xpath(passwd_xpath).send_keys("passwd")

clik_xpath = '/html/body/pd-root/div/div/ng-component/main/section/ng-component/ng-component/form/section/pd-button/button'
driver.find_elements_by_xpath(clik_xpath).click()

# except Exception as ex:
#     print(ex) 

