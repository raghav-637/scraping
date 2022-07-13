import undetected_chromedriver.v2 as uc
import time
from typing import TextIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType


def main(url):
 options = webdriver.ChromeOptions()
 options.headless = True

 driver = uc.Chrome(options=options)

 driver.get(url)
 driver.delete_all_cookies()
 time.sleep(5)
 data=driver.page_source
 #print(data)
 soup = BeautifulSoup(data, 'html.parser')
 title = soup.find("h3", class_="header-primary--pd")
 aa = (title.text.strip() if title else "not given")
 print(aa)

 title2 = soup.find("h3", class_="header-secondary--pd")
 aa2 = (title2.text.strip() if title2 else "not given")
 print(aa2)

 images=soup.find_all("img",class_="Thumbnail_thumbnailImg__2X_Hx")
 img_list=[]
 for image in images:
  img_list.append(image.get("src"))
 print(img_list)


 price=soup.find("div",class_="PrceTxt")
 pri=(price.text.strip() if price else "not given")
 print(pri)
 try:

  prod = soup.find("table", class_="spec-table--pd").find_all("td",class_="attr-cell--table divider--spec-tbl")

  specs = soup.find("table", class_="spec-table--pd").find_all("td",class_="divider--spec-tbl value-cell--table")

  i = 0

  while i < len(prod):

   j = 0

   while j < len(specs):
    z = (prod[i].text if prod else "not given")
    print(z)

    i += 1

    x = (specs[j].text if specs else "not given")
    print(x)

    j += 1
    save_details: TextIO = open("mc-master-git-chck.txt", "a+", encoding="utf-8")
    save_details.write("\n"+url+"\t"+aa+"\t"+aa2+"\t"+" , ".join(img_list)+"\t"+pri+"\t"+z+"\t"+x)
    save_details.close()
    print("\n**Record stored into txt file.**")
 except:
     pass

if __name__ == '__main__':
    list=['https://www.mcmaster.com/2427K42']
    for x in range(0,len(list)):
     print(x)
     print(list[x])
     main(list[x])


