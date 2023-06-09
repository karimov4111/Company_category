import time
import sys
import requests
import csv 
import pandas
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
url="https://www.1800d2c.com/all-brands"
driver.get(url)
time.sleep(3)
button = driver.find_element(By.XPATH, '//div/a[@data-w-id="a4a97fb1-838f-bdd4-d228-e7585444fc3b"]').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,1000)", "")
time.sleep(2)
driver.execute_script("window.scrollBy(0,8000)", "")
time.sleep(2)
soup=BeautifulSoup(driver.page_source, 'html.parser')
divs = soup.find_all("div", class_="cardbrand w-dyn-item")
all_url = []
deta = []
for x in divs:
    k = x.find("a")["href"]
    all_url.append(k)
current_url = "https://www.1800d2c.com/"
n = 0
for ur in all_url:
    url = current_url+str(ur)
    time.sleep(1.5)
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'html.parser')
    title = soup.find("h1", class_="heroh1").text.strip()
    categories = soup.find("div", class_="wrap toolhorizontal").text.strip()
    divs = soup.find_all("h2", class_="cardheader tool")
    numbers = soup.find("div", class_="numbers").text.strip()
    tools = ""
    for a in divs:
        tools += f"{a.text.strip()} \n"
    deta.append(
        {
        "company_name": title,
        "url": url,
        "category": categories,
        "tools": tools
        }
    )
    n+=1
    print(n)
df = pandas.DataFrame(data=deta)
df.to_csv(
    sys.argv[1], encoding="utf-8",
    line_terminator="\n",
    quotechar='"',
    quoting=csv.QUOTE_ALL,
    index=False)

