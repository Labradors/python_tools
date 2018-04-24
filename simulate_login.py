import requests
from selenium import webdriver
from PIL import Image
import json
import os
import extract_images
import time



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
            wd.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]').click()
            wd.find_element_by_id('loginname').send_keys(login_name)
            wd.find_element_by_id('nloginpwd').send_keys(login_password)
            wd.find_element_by_id('loginsubmit').click()
            time.sleep(3)
            wd.get_screenshot_as_file('jd_login.png')
             # 图片地址
            # vert = wd.find_element_by_id('JD_Verification1').get_attribute('src')
            # print(vert)
            # 下载图片
            # save_img(vert)
            screen_img()
            # 解析图片文字并且填如
            im = Image.open("pic.gif")
            verification_code = extract_images.extract_image(im)
            print("当前验证码："+verification_code)
            if verification_code is not None:
                wd.find_element_by_id('authcode').send_keys(verification_code)
                wd.find_element_by_id('loginsubmit').click()
                wd.get('https://item.jd.com/6171814.html')
                # 点击预约商品
                wd.find_element_by_id('btn-reservation').click()
                # req = requests.Session() #构建Session
                # cookies = wd.get_cookies() #导出cookie
                # for cookie in cookies:
                #     req.cookies.set(cookie['name'],cookie['value']) #转换cookies
                # test = req.get('待测试的链接')
            else:
                print('验证码识别错误...')
        finally:
            wd.close()

def save_img(url):
    img = requests.get(url)
    with open('pic.png', 'wb') as file:
        file.write(img.content)


def screen_img():
    im = Image.open("jd_login.png")
    img_size = im.size
    print("图片宽度和高度分别是{}".format(img_size))
    # 截取图片中一块宽和高都是250的
    x = 1890
    y = 754
    w = 139
    h = 66
    region = im.crop((x, y, x+w, y+h))
    region.save("pic.gif")

if __name__ == '__main__':
    login()