# PChome 24h 自動化搶購

## 起源

* 自從開始遠距教學後，就無法止住我想組電腦的慾望，但礙於前段時間虛擬貨幣大漲，顯示卡一卡難求，3070ti 根本搶不到。於是就想寫個程式看能不能在 6/18 搶到顯卡，結果我在 6/16 前找了很久都沒找到
 PChome 要賣顯卡的消息，結果 6/17 消息才出來而我沒看到...。
* 本程式碼原作者為 [jumpingchu](https://github.com/jumpingchu/PChome-AutoBuy)，此為純作業用之修改版，並增加及改善以下功能:
    1. 改善有時無法按到購物車按鈕(改為直接前往購物車連結)
    2. 加入定時功能(到達指定時間使程式自動執行搶購)
    3. 加入機制預防 PChome 的時差 [參考資料](https://blog.jiatool.com/posts/pchome_spider01/)
    4. 將程式碼函式化，並修改部分執行流程，降低搶購所需時間
    5. 將結帳畫面的資料填入功能完善
* 本程式利用 Selenium API 來抓取網頁資料，並利用 .click() 函式來模擬滑鼠點擊，以模擬從點開商品頁面到下單之間的所有動作。

## 功能

* 自動化快速搶購 PChome 24h 指定網頁之商品，並自動填入結帳資料，以快速完成購買動作。

## 使用工具

* Python
* Selenium
    ```bash
    $ pip install selenium
    ```
* Requests
  * 安裝 Python 2 的 requests 模組
    ```bash
    $ pip install requests
    ```
  * 安裝 Python 3 的 requests 模組
    ```bash
    $ pip3 install requests
    ```

## 使用方法

1. 將 repo 複製到自己的資料夾
    ```bash
    $ git clone https://github.com/sheway/PChome-AutoBuy.git
    ```

2. 下載 `chromedriver.exe` 並放在同個資料夾內 ([前往下載](http://chromedriver.storage.googleapis.com/index.html))
   
3. 於 `settings.py` 事先填入各項資料。

4. 請先執行 `pchome_autobuy.py` 的 217 行以登入帳戶，登入成功後可將此行註解。

5. 於 `pchome_autobuy.py` 的 224 行輸入搶購時間(24時制)。
   
6. 執行程式
    ```bash
    $ python pchome_autobuy.py
    ```

## 程式執行流程
1. 登入帳戶
2. 等待搶購時間
3. 判斷商品是否開賣
4. 將商品加入購物車
5. 前往購物車
6. 點選一次付清
7. 手動點擊繼續 (非必要)
8. 填入各項資料
9. 勾選同意
10. 點擊送出訂單

## 程式製作過程
1. 登入帳戶
    * 使用 .get 將 chrome 模擬器前往 PChome 登入頁面
    ```bash
    driver.get("https://ecvip.pchome.com.tw/login/v3/login.htm?")
    ```
    * 使用 .find_element_by_id 尋找帳號密碼的欄位
    ```bash
    elem = driver.find_element_by_id('loginAcc')
    ```
    * 使用 .send_keys 將帳號密碼填入相對應欄位
    ```bash
    elem.send_keys('我的帳號')
    ```
    ![1624338072127_new](https://user-images.githubusercontent.com/67420772/122872112-8960a480-d362-11eb-8f3e-c04c6c832360.jpg)

2. 等待搶購時間
    * 使用 time.strftime('%H_%M_%S') 得到目前的時間，並使用 while 迴圈等待
    ![1624338072127_new](https://user-images.githubusercontent.com/67420772/122895158-6cd06680-d37a-11eb-9c23-202cc95025f5.jpg)

3. 判斷商品是否開賣
    * 使用 requests.get(url) 來得到商品目前資訊，並判斷 ButtonType 是否為 ForSale
    * 未開賣:
    ![1624338211290](https://user-images.githubusercontent.com/67420772/122866331-59150800-d35a-11eb-994b-b54b84ef3e24.jpg)
    * 已開賣:
    ![1624338197650](https://user-images.githubusercontent.com/67420772/122866324-561a1780-d35a-11eb-8f78-9a22b9594c95.jpg)

4. 將商品加入購物車
    * 使用 .get 將 chrome 模擬器前往商品頁面
    ```bash
    driver.get("你的商品連結")
    ```
    * 使用 WebDriverWait 等待指定容器加載好
    ```bash
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@id='ButtonContainer']/button")) #ButtonContainer為 PChome 定義的變數名稱
    )
    ```
    * 使用 .find_element_by_xpath 尋找加入購物車按鈕並利用 .click() 來模擬按下加入按鈕
    ```bash
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
    ``` 
    ![1624338566818](https://user-images.githubusercontent.com/67420772/122867931-da6d9a00-d35c-11eb-9592-abc7547b5790.jpg)

5. 前往購物車
    * 使用 .get 將 chrome 模擬器前往購物車頁面
    ```bash
    driver.get("購物車頁面連結")
    ```
    ![1624338611067](https://user-images.githubusercontent.com/67420772/122867960-e3f70200-d35c-11eb-874f-89a0e6974cb3.jpg)

6. 點選一次付清
    * 使用 WebDriverWait 等待存有'一次付清'容器加載好
    ```bash
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@id='ButtonContainer']/button")) #ButtonContainer為 PChome 定義的變數名稱
    )
    ```
    ![1624338611067_new](https://user-images.githubusercontent.com/67420772/122868093-0db02900-d35d-11eb-84f8-60ad394176cc.jpg)

7. 手動點擊繼續 (非必要)
    ![1624338611067_new](https://user-images.githubusercontent.com/67420772/122868189-36382300-d35d-11eb-8e6f-6e1a274d0a13.jpg)

8. 填入各項資料
    * 重複使用 .find_element_by_id 以及 .send_keys 填入資料
    ```bash
    elem = driver.find_element_by_id('資料欄位')
    elem.send_keys(資料變數名稱)
    ```
![1624339156506](https://user-images.githubusercontent.com/67420772/122868374-74cddd80-d35d-11eb-8870-b89419a0d27c.jpg)
9. 勾選同意
10. 點擊送出訂單

## 執行結果
[前往 Youtube ](https://youtu.be/-x1nxdC0vX4)

## Pseudocodes
1. LoginAccount()
2. while flag:
       if current_time == start_buy_time:
           while not get_products_sale_status():
           Try:
               Start_to_buy()
           Exception:
               print Exception
       else:
           wait 1 second
           print current_time 

## 函式說明
1. login_acc(): 第一次使用時，用來自動化登入 pchome24h。
2. get_products_sale_status(): 到指定時間後，為避免電腦時間與 pchome24h 時間有時差，須等此函式確認商品是否開賣。
3. run_script(): 確認商品開賣後，執行此 function 以開始搶購。

## 注意事項
1. 本程式碼原作者為 [jumpingchu](https://github.com/jumpingchu/PChome-AutoBuy)，已經與原創作者取得授權作為純作業用。

2. 可以先拿其他的商品連結做測試，以防搶購時的突發狀況或錯誤（但請記得馬上取消訂單！）。
   
3. `settings.py` 內的 CHROME_PATH 可讓 chrome 記住登入資訊，可提升搶購速度，建議使用。

4. 由於近期貨物過多，大多商品皆會跳出"訂單不受24小時到貨時間限制"，**請手動點擊繼續** (2021/06/19)。

5. 本程式碼單純是提供搶購足夠數量的商品為主，**禁止用於大量收購並哄抬價格的黃牛行為！**。

## 待辦事項
1. 本程式碼 **尚未適用** 於數量多於１或必須選擇顏色或樣式的商品。
2. 預防 pchome 時差機制 (get_products_sale_status) 在執行 7\~9 次後就會被伺服器擋住，目前尚無有效方法解決，但通常 2\~3 次後就會開始搶。
3. `pchome_autobuy.py` 的 206 行為不開啟實體瀏覽器背景執行，但經實測無法成功。
4. 想加入 Line Bot 來定時幫我開搶

## 參考資料
* [https://blog.jiatool.com/posts/pchome_spider01/](https://blog.jiatool.com/posts/pchome_spider01/)
* [https://github.com/jumpingchu/PChome-AutoBuy](https://github.com/jumpingchu/PChome-AutoBuy)
* [https://www.itread01.com/content/1496631486.html](https://www.itread01.com/content/1496631486.html)
* [http://lms.tzuchi.com.tw/epaper/artical/index.php?id=file/48/digiinfo_3](http://lms.tzuchi.com.tw/epaper/artical/index.php?id=file/48/digiinfo_3)
