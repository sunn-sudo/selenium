import time
import datetime
from selenium import webdriver

driver = webdriver.Chrome()

# ログイン処理
driver.get('https://note.com/login')
time.sleep(3)

# クッキーを利用した自動ログイン
driver.add_cookie(
    {'name': '[クッキー名]',
     'value': '[コード値]',
     'domain': '.note.com',
     'path': '/'
     })

count = 0
for num in range(10):
    driver.get('https://note.com/[noteのアカウントID]/followers?page=' + str(num+1))
    buttons = driver.find_elements_by_css_selector(
        'div.m-userListItem__action > button.a-button')
    time.sleep(10)

    try:
        # ボタンの数分クリック
        for button in buttons:
            time.sleep(5)
            if button.text == "フォロー":
                # ボタンをクリック
                button.click()
                count = count + 1
            if count == 5:
                # 5回フォローしたら正常終了
                print(str(datetime.datetime.today()) + ' 正常終了:クリック回数 → ' + str(count))
                driver.quit()

    except:
        # 5回フォローに失敗した場合
        if count != 5:
            print(str(datetime.datetime.today()) + ' エラー発生:クリック回数 → ' + str(count))
        driver.quit()

print(str(datetime.datetime.today()) + ' 正常終了:クリック回数 → ' + str(count))
driver.quit()
