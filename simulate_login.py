import requests
from selenium import webdriver
import json



# 读取account.json 转为字典
def account():
    with open("./account.json",'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict

def readUrls():
    pass

# 登陆
def login():
    account_list = account()
    for account_dist in account_list:
        login_name = account_dist['username']
        login_password = account_dist['password']
        try:
            wd = webdriver.Chrome() 
            loginUrl = 'https://passport.jd.com/new/login.aspx' 
            wd.get(loginUrl)
            wd.find_element_by_id('loginname').send_keys(login_name)
            wd.find_element_by_id('nloginpwd').send_keys(login_password)
            wd.find_element_by_id('loginsubmit').click()
            wd.get('https://item.jd.com/6171814.html')
            # 点击预约商品
            wd.find_element_by_id('btn-reservation').click()
            # req = requests.Session() #构建Session
            # cookies = wd.get_cookies() #导出cookie
            # for cookie in cookies:
            #     req.cookies.set(cookie['name'],cookie['value']) #转换cookies
            # test = req.get('待测试的链接')
        finally:
            wd.close()