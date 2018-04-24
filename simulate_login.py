import requests
from selenium import webdriver

wd = webdriver.Chrome() #构建浏览器
loginUrl = 'http://www.weibo.com/login.php' 
wd.get(loginUrl) #进入登陆界面
wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('userword') #输入用户名
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('password') #输入密码
wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click() #点击登陆
req = requests.Session() #构建Session
cookies = wd.get_cookies() #导出cookie
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value']) #转换cookies
test = req.get('待测试的链接')