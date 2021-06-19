# PChome 24h 自動化搶購

## 功能

* 自動化快速搶購 PChome 24h 指定網頁之商品

## 使用工具

* Python
* Selenium
    ```bash
    $ pip install selenium
    ```

## 使用方法

1. 將 repo 複製到自己的資料夾
    ```bash
    $ git clone https://github.com/jumpingchu/PChome-AutoBuy.git
    ```

2. 下載 `chromedriver.exe` 並放在同個資料夾內 ([前往下載](http://chromedriver.storage.googleapis.com/index.html))
   
3. 在 `settings.py` 填入資料（請保管好個資）
   
4. 執行程式
    ```bash
    $ python pchome_autobuy.py
    ```

## 注意事項
1. 本程式碼原作者為 [jumpingchu](https://github.com/jumpingchu/PChome-AutoBuy)，此為純作業用之修改版，並增加及改善以下功能:
    1-1. 改善有時無法按到購物車按鈕(改為直接前往購物車連結)
    1-2. 加入定時功能(到達指定時間使程式自動執行搶購)
    1-3. 加入機制預防 pchome 的時差

2. 可以先拿其他的商品連結做測試，以防搶購時的突發狀況或錯誤（但請記得馬上取消訂單！）
   
3. `settings.py` 內的 CHROME_PATH 可讓 chrome 記住登入資訊，可提升搶購速度，建議使用
   
4. 本程式碼 **尚未適用** 於數量多於１或必須選擇顏色或樣式的商品

5. 由於近期貨物過多，大多商品皆會跳出"訂單不受24小時到貨時間限制"，請手動點擊繼續(2021/06/19)

6. 本程式碼單純是提供搶購足夠數量的商品為主，**禁止用於大量收購並哄抬價格的黃牛行為！**

## 程式執行流程
1. 登入帳戶
2. 輸入搶購時間
3. 判斷商品是否開賣
4. 將商品加入購物車
5. 前往購物車
6. 點選一次付清
7. !!!手動點擊繼續!!!
8. 填入各項資料(可於 `settings.py` 事先填入以加速結帳時間)
9. 勾選同意
10. 點擊送出訂單

## 程式事前準備工作(第一次使用)
1. 於 `settings.py` 事先填入各項資料(注意 product_id 為商品連結 https://24h.pchome.com.tw/prod/ 之後的商品代碼)
2. 請先執行 214 行以登入帳戶
3. 於 `pchome_autobuy.py` 的 220 行輸入搶購時間(24時制)

