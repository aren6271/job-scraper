import requests
from bs4 import BeautifulSoup
from func import *
import mechanize
import time

keyword = '2022 summer software engineering internship'

# while True:
url = "https://www.indeed.com/?from=gnav-jobsearch--jasx"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}

br = mechanize.Browser()
br.open(url)
br.select_form(nr=0)
print(br.form)
br['q'] = '2022 summer software engineering internship'
br['l'] = 'California'
response = br.submit()

print(response.geturl())

soupResponse = requests.get(response.geturl(), headers=headers)
soup = BeautifulSoup(soupResponse.text, "lxml")

soupHead = soup.head

for num, parents in enumerate(soupHead.find_all_next('td', 'resultContent')):
  title = parents.find(has_title).get_text()
  companyName = parents.find('span', 'companyName').get_text()
  print(f'{num+1}. {companyName} - {title}')


# if (str(soup).find("A") == -1):
#   print("No Andy Yet")
#   time.sleep(5)
#   continue
# else:
#   print('I found Andy!')
#   break