import requests
import pandas as pds
import pyautogui as pygui
import random
import sqlite3 as sql3
import time

from bs4 import BeautifulSoup
from func import *
from rand_mouse import *

#####



#####

keyword = '2023 winter software engineering internship'
locations = ['California', 'Seattle']
location = locations[0]

companyList = []
page, currJobNum, jobLimit = 0, 0, 50

position = ['Software Development', 'Software Engineer', 'Software Engineering']
jobType = ['Intern', 'intern', 'Internship',' internship']

# while (currJobNum < jobLimit):
url = f"https://www.indeed.com/jobs?q={keyword}&l={location}&filter=0&start={page*10}"
headers = {
  "Accept": "application/json",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-US,en;q=0.9",
  "Sec-Ch-Ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "same-origin",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

soupResponse = requests.get(url, headers=headers)
# time.sleep(random.randrange(10,20))
soup = BeautifulSoup(soupResponse.text, "lxml")

soupHead = soup.head

print(soupHead)
# for num, parents in enumerate(soupHead.find_all_next('td', 'resultContent')):
#   title = parents.find(has_title).get_text()
#   print(title)
#   if any(words in title for words in position) and any(words in title for words in jobType):
#     companyName = parents.find('span', 'companyName').get_text()
#     print(f'{num+1}. {companyName} - {title}')

#     company = [title, companyName]
#     companyList.append(company)

# print(f'PAGE {page+1}')
# page += 1
# currJobNum += 10


# Creating Database

conn = sql3.connect('job_db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS jobs (title text NOT NULL UNIQUE PRIMARY KEY, company text NOT NULL UNIQUE)')
conn.commit()

df = pds.DataFrame(data = companyList)

df.to_sql('jobs', conn, if_exists='replace')


