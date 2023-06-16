import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)



page = requests.get(START_URL)
soup = BeautifulSoup(page.content,'html.parser')


table=soup.find_all("table",attrs={"class":"wikitable sortable"})[2]




# tbody = soup.find('tbody')
tr_tag_list =table.find_all('tr')

temp_list = [] 
final_list = []


# # print(tr_tag_list)

for tr_tag in tr_tag_list:
    td_tag_list = tr_tag.find_all('td')
    row=[i.text.rstrip() for i in td_tag_list]
    
    temp_list.append(row)
    

names = []
distance = []
mass = []
radius = []    
for index,row in enumerate(temp_list):

    if index != 0:
        names.append(row[0])
        distance.append(row[5])
        mass.append(row[7])
        radius.append(row[8])
#final_list.append(temp_list)
# print(final_list)    

headers = ['StarName','Radius','Mass','DistanceData']
data = pd.DataFrame(list(zip(names,distance,mass,radius)),columns = headers)

print(type(data['Mass']))

#data.to_csv('Data.csv', index=True, index_label="id")

