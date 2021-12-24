import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
options = webdriver.ChromeOptions()    #Chrome yi görmek  istiyorsan burayı sil 
options.add_argument('--headless')     #chrome yi görmek istiyorsan burayı sil
browser = webdriver.Chrome(options=options) #chromeyi görmek istiyorsan browser = webdriver.Chrome() yaz
url = "https://www.nesine.com/iddaa/canli-skor/basketbol"
browser.get(url)
time.sleep(4)
hometeams = []
awayteams = []
homegol = []
awaygol = []
ssxp = browser.find_elements(By.CSS_SELECTOR, ".home-team")
for e in ssxp:
    if len(ssxp) < 2:
        print("kirmizi kart sayisi : ", e)
    else:
        hometeams.append(e.text)
        print(e.text)
ssxp2 = browser.find_elements(By.CSS_SELECTOR, ".away-team")
for el in ssxp2:
    if len(ssxp2) < 2:
        print("kirmizi kart sayisi : ", el)
    else:
        awayteams.append(el.text)
        print(el.text)
ssxp3 = browser.find_elements(By.CSS_SELECTOR, "span.home-score.no-animation")
for ele in ssxp3:
    if ele == '':
        homegol.append(ele.text)
        homegol.append(ele.text)
    else:
        homegol.append(ele.text)
        print(ele.text,"-")
ssxp4 = browser.find_elements(By.CSS_SELECTOR, "span.away-score.no-animation")
for elem in ssxp4:
    if elem == '':
        awaygol.append(elem.text)
        awaygol.append(elem.text)
    else:
        awaygol.append(elem.text)
        print("-",elem.text)
i = 0
sayimk = len(hometeams)
while (i < sayimk):
    goinurl = "http://localhost/bettilt/adm/mcprc.php?evtakim="+hometeams[i]+"&deplasman="+awayteams[i]+"&skor="+homegol[i]+"-"+awaygol[i]+"&ms1=0.00&ms2=0.00&msx=0.00"
    browser.execute_script("window.open(arguments[0])", goinurl)
    browser.switch_to.window(browser.window_handles[0])
    print(hometeams[i], homegol[i], "-", awaygol[i], awayteams[i])
    i += 1
print("bol sans")
