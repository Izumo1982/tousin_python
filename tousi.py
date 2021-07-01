from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib
import os
import s_mail
import tousin_data

def tousin():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])


    tositable = tousin_data.table()

    pr = "　　愛　称　　｜価   額｜ 増　減 ｜ 評価金額 ｜総額の増減｜\n------------------------------------------------------------"
    ttl = 0
    zougen = 0

    for fand,url,kutisu,aisyo in tositable:
            print("ファンド名" + fand)
            print(url)
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(url)
            time.sleep(1)

            soup = BeautifulSoup(driver.page_source, "html.parser")
            mon = 0
            for element1 in soup.find_all(class_= "h3 font-weight-bold"):
                    hyo = element1.get_text(strip=True).replace(',', '')

            for element2 in soup.find_all(class_= "h3 font-weight-bold mb-0"):
                    mon = element2.get_text(strip=True).replace(',', '')

            pn = ""
                
            if soup.find(class_= "fa fa-long-arrow-down") == None:
                    print("up")
                    pn = "＋"
                    kob = int(mon) * kutisu / 10000
                    zougen += kob 

            if soup.find(class_= "fa fa-long-arrow-up") == None:
                    print("down")
                    pn = "－"
                    kob = int(mon) * kutisu / 10000 * -1
                    zougen += kob

            if pn == "":
                    print("flat")
                    pn = "±"
                    zougen = 0
                    
            meigara = int(hyo) * int(kutisu) / 10000
            ttl += meigara

            hyo = ("{:,}".format(int(hyo))).rjust(7, ' ')
            mon = ("{:,}".format(int(mon))).rjust(6, ' ')
            meigara = ("{:,.0f}".format(meigara)).rjust(10, ' ')
            kob = ("{:,.0f}".format(kob)).rjust(10, ' ')
            
            pr = pr + "\n" + aisyo+ "｜" + hyo+ "｜" + pn + mon + "｜"  + meigara + "｜" + kob + "｜"
                    
            driver.close()


    zougen = "{:,.0f}".format(zougen)
    ttl = "{:,.0f}".format(ttl)

    pr = pr + "\n------------------------------------------------------------\n今日の増減額：" + zougen + "\n合計評価額　　：" + ttl

    s_mail.sending_mail("send@yyyy.com", "recieve@xxxx.com", "投資信託", pr)
    print(pr)
