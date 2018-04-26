import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
import json
import os
import extract_images
import time
import code



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
            __options = webdriver.ChromeOptions()
            __options.add_argument(
            'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"')
            wd = webdriver.Chrome(chrome_options=__options)
            loginUrl = 'https://passport.jd.com/new/login.aspx' 
            wd.get(loginUrl)
            title = '京东-欢迎登录'
            while(title == '京东-欢迎登录'):
                wd.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
                wd.find_element_by_id('loginname').send_keys(login_name)
                wd.find_element_by_id('nloginpwd').send_keys(login_password)
                wd.find_element_by_id('loginsubmit').click()
                time.sleep(3)
                # wd.get_screenshot_as_file('./jd_login.png')
                # screen_img()
                # # 解析图片文字并且填如
                # im = Image.open("pic.png")
                # extract = code.binarize(im)
                # verification_code = code.extractRe(extract)
                title = wd.find_elements_by_xpath('/html/head/title')
                if title == '京东-欢迎登录':
                    verification_code = verification()
                    if verification_code == None:
                        wd.refresh()
                    else:
                        print("当前验证码："+verification_code)
                        if verification_code is not None:
                            wd.find_element_by_id('authcode').send_keys(verification_code)
                            wd.find_element_by_id('loginsubmit').click()
                            time.sleep(0.5)
                            title = wd.find_elements_by_xpath('/html/head/title')
                            time.sleep(2)
                            # 进入订单列表界面
                            # wd.find_element_by_css_selector('#ttbar-login > div.dt.cw-icon > a').click()
                            # time.sleep(5)
                            # 进入我的预约界面
                            # wd.find_element_by_css_selector('#_MYJD_yushou > a').click()
                            wd.get('https://yushou.jd.com/member/qualificationList.action')
                            time.sleep(20)
                            # 点击预约商品
                            # wd.find_element_by_id('btn-reservation').click()
                            # req = requests.Session() #构建Session
                            # cookies = wd.get_cookies() #导出cookie
                            # for cookie in cookies:
                            #     req.cookies.set(cookie['name'],cookie['value']) #转换cookies
                            # test = req.get('待测试的链接')
                        else:
                            print('验证码识别错误...')
                else:
                     wd.get('https://yushou.jd.com/member/qualificationList.action')
                     time.sleep(20)
        finally:
            wd.close()

def save_img(url):
    img = requests.get(url)
    with open('pic.png', 'wb') as file:
        file.write(img.content)

def verification():
    x = input('请输入验证码： ')
    return x


def screen_img():
    im = Image.open("jd_login.png")
    img_size = im.size
    print("图片宽度和高度分别是{}".format(img_size))
    # 截取图片中一块宽和高都是250的
    x = 497
    y = 861
    w = 107
    h = 59
    region = im.crop((x, y, x+w, y+h))
    region.save("pic.png")

if __name__ == '__main__':
    login()