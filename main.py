import requests
import pandas as pds
import random
from bs4 import BeautifulSoup
from func import *
import time

keyword = '2022 summer software engineering internship'
location = 'California'

companyList = []
page, currJobNum, jobLimit = 0, 0, 50

masterCompanyDF = pds.read_csv("./masterCompanyData.csv")

position = ['Software Development', 'Software Engineer', 'Software Engineering']
jobType = ['Intern', 'intern', 'Internship',' internship']

while (currJobNum < jobLimit):
  url = f"https://www.indeed.com/jobs?q={keyword}&l={location}&filter=0&start={page*10}"
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}

  soupResponse = requests.get(url, headers=headers)
  time.sleep(random.randrange(10,13))
  soup = BeautifulSoup(soupResponse.text, "lxml")

  soupHead = soup.head

  for num, parents in enumerate(soupHead.find_all_next('td', 'resultContent')):
    title = parents.find(has_title).get_text()
    if any(words in title for words in position) and any(words in title for words in jobType):
      companyName = parents.find('span', 'companyName').get_text()
      print(f'{num+1}. {companyName} - {title}')

      company = [title, companyName]
      companyList.append(company)
  
  print(f'PAGE {page+1}')
  page += 1
  currJobNum += 10

masterCompanyDF = pds.DataFrame(data = companyList)
masterCompanyDF.to_csv("./masterCompanyData.csv")


