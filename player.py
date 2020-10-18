import requests
#Importing beautiful soup for scraping
from bs4 import BeautifulSoup

PlayerID=int(input('Enter Player Id: '))

url=f'http://howstat.com/cricket/Statistics/Players/PlayerOverview_ODI.asp?PlayerID={PlayerID}'

data = requests.get(url)
html_code = data.content
# print(html_code)

#Parser
soup = BeautifulSoup(html_code, 'html.parser')

Scraping_Factors = soup.findAll(class_='FieldName')
Scraping_Values = soup.findAll(class_='FieldValue')

Factors=[]
Values=[]

for every_value in Scraping_Factors:
    Factors.append(every_value.getText(strip=True))

for every_value in Scraping_Values:
    Values.append(every_value.getText(strip=True))

player={}

for every in range(15):
    player.update({Factors[every+6]:Values[every]})

print(player)