import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import URL, CHROME_PATH, loginAcc, loginPwd, BuyerName, BuyerGender, BuyerSSN, BirthYear, BirthMonth, BirthDay, CardNum_single, multi_ThruMonth, multi_ThruYear, multi_CVV2Num, BuyerMobile, BuyerAddrCity, BuyerAddrRegion, BuyerAddr
product_id = ''

def login_acc():
    driver.get("https://ecvip.pchome.com.tw/login/v3/login.htm?")  #前往登入頁面
    WebDriverWait(driver, 20).until( #等待帳號輸入框加載完畢
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    elem = driver.find_element_by_id('loginAcc') #尋找帳號輸入框
    elem.clear()
    elem.send_keys(loginAcc) #輸入帳號
    elem = driver.find_element_by_id('loginPwd') #尋找密碼輸入框
    elem.clear()
    elem.send_keys(loginPwd) #輸入密碼
    elem.send_keys(Keys.ENTER)
    time.sleep(4)

def run_script():
    print("放入購物車")
    WebDriverWait(driver, 20).until( #等待放入購物車按鈕加載完畢
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@id='ButtonContainer']/button"))
    )
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click() #按下放入購物車按鈕

    print("前往購物車")
    driver.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")  #直接前往購物車

    #前往結帳 (一次付清) ### (要使用 JS 的方式 execute_script 點擊)
    print("前往結帳")
    WebDriverWait(driver, 20).until( #等待'一次付清'按鈕的 class 加載完畢
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath( #按下'一次付清'按鈕
        "//li[@class='CC']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)


    #BuyerName, BuyerGender, BuyerSSN, BirthYear, BirthMonth, BirthDay, CardNum_single, multi_ThruMonth, multi_ThruYear, multi_CVV2Num, BuyerMobile, BuyerAddrCity, BuyerAddrRegion, BuyerAddr
    print("填入各項資料")

    #填入買家姓名
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@id='BuyerName']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='BuyerName']")
    elem.clear()
    elem.send_keys(BuyerName)

    #填入買家性別
    if BuyerGender == "男":
        driver.find_element_by_xpath("//input[@value='M']").click()
    else:
        driver.find_element_by_xpath("//input[@value='F']").click()

    # 填入買家身分證
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@id='BuyerSSN']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='BuyerSSN']")
    elem.clear()
    elem.send_keys(BuyerSSN)

    # 填入買家生日年月日
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthYear']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthYear']")
    elem.clear()
    elem.send_keys(BirthYear)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthMonth']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthMonth']")
    elem.clear()
    elem.send_keys(BirthMonth)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthDay']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthDay']")
    elem.clear()
    elem.send_keys(BirthDay)

    #填入買家信用卡卡號
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='CardNum_single']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='CardNum_single']")
    elem.clear()
    elem.send_keys(CardNum_single)

    #填入買家信用卡到期月
    parent = driver.find_element_by_id("multi_ThruMonth")
    path = './/option[@value="' + multi_ThruMonth + '"]'
    parent.find_element_by_xpath(path).click()

    #填入買家信用卡到期年
    parent = driver.find_element_by_id("multi_ThruYear")
    path = './/option[@value="' + multi_ThruYear + '"]'
    parent.find_element_by_xpath(path).click()

    #填入買家信用卡末三碼
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.clear()
    elem.send_keys(multi_CVV2Num)

    #填入買家手機
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BuyerMobile']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BuyerMobile']")
    elem.clear()
    elem.send_keys(BuyerMobile)

    #填入買家信用卡帳單地址(縣市)
    parent = driver.find_element_by_id("BuyerAddrCity")
    city_array = ["基隆市", "臺北市", "新北市", "桃園市", "新竹市", "新竹縣", "苗栗縣", "臺中市", "彰化縣", "南投縣", "雲林縣", "嘉義市", "嘉義縣", "臺南市", "高雄市", "屏東縣", "臺東縣", "花蓮縣", "宜蘭縣", "澎湖縣", "金門縣", "連江縣"]
    path = './/option[@value="' + str(city_array.index(BuyerAddrCity)) + '"]'
    parent.find_element_by_xpath(path).click()

    #填入買家信用卡帳單地址(區)
    parent = driver.find_element_by_id("BuyerAddrRegion")
    path = './/option[@data-region="' + BuyerAddrRegion + '"]'
    # print("BuyerAddrRegion", path)
    parent.find_element_by_xpath(path).click()

    #填入買家信用卡帳單地址(剩餘地址)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BuyerAddr']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BuyerAddr']")
    elem.clear()
    elem.send_keys(BuyerAddr)

    #取消願意收到PChome商品特惠通知
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='RecvAd']"))
    )
    driver.find_element_by_xpath("//input[@name='RecvAd']").click()

    #清除記住結帳資訊加速下次使用
    WebDriverWait(driver, 20)
    driver.find_element_by_xpath("//input[@name='remCreditCard']").click()

    driver.find_element_by_xpath("//input[@value='P']").click()
    driver.find_element_by_id('syncData').click()
    driver.find_element_by_id('syncData').click()

    #勾選同意
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='chk_agree']"))
    )
    driver.find_element_by_xpath("//input[@name='chk_agree']").click()

    # ### 送出訂單 ### (要使用 JS 的方式 execute_script 點擊)
    # WebDriverWait(driver, 20).until(
    #     expected_conditions.element_to_be_clickable(
    #         (By.XPATH, "//a[@id='btnSubmit']"))
    # )
    # button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
    # driver.execute_script("arguments[0].click();", button)

def get_products_sale_status(): #利用 requests 來跟 server 索要商品資訊
    url_get = "https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/button&id=" + product_id
    data = requests.get(url_get)
    print(data.text)
    a = data.text.split(',')
    for i in range(len(a)):
        if a[i].find("ButtonType") > -1:
            num = i
    # print(a[num])
    cur_status = a[num].split(':')[1].find("ForSale") #若 'ButtonType' 為 'ForSale' 代表商品開賣了
    if cur_status > -1:
        driver.get(url)
        return True
    else:
        return False


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PATH)
    # options.add_argument("--headless")  # 不開啟實體瀏覽器背景執行
    driver = webdriver.Chrome(
        executable_path='chromedriver.exe', chrome_options=options)
    driver.set_page_load_timeout(120)
    product_id = URL.split("/prod/")[1]
    if product_id.find("?") > -1:
        product_id = product_id.split("?")[0]
    # print(product_id)
    url = "https://24h.pchome.com.tw/prod/" + product_id

    #登入帳戶
    login_acc()

    driver.get(url)
    flag = True
    number = 0
    while flag:
        curr_time = time.strftime('%H_%M_%S')
        if curr_time == '14_14_50':  # 請輸入開始搶購的時間(24時制)
            while not get_products_sale_status():  # 預防pchome的時差
                # print(number)
                number += 1
            print("開始運行腳本:")
            try:
                run_script()
                flag = False
            except Exception as e:
                print(e)
        else:
            time.sleep(1)
            print(curr_time)
