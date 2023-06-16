import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
# browser = webdriver.Chrome("chromedriver.exe")
# browser.get(START_URL)

time.sleep(2)

scrape_data = []

def scrape():

   
        print('Scrapping page ' )

        soup = BeautifulSoup(browser.page_source,"html.parser")

        bright_star_table = soup.find("table" , attrs ={"class" , "wikitable"} )

        table_body = bright_star_table.find("tbody")

        table_rows = table_body.find_all('tr')
       # print(table_rows)
        
        for row in table_rows:
                table_cols = row.find_all('td')
               
                # Get data from
                temp_list = []

                for col_data in table_cols:
                
                    data = col_data.text.strip()
                    
                    temp_list.append(data)

                scrape_data.append(temp_list) 

                stars_data = []

        for i in range(0,len(scrape_data)):

                
                
                Stars_names = scrape_data[i][1]
                Distance = scrape_data[i][3]
                Mass = scrape_data[i][5] 
                Radius = scrape_data[i][6]
                Lum = scrape_data[i][7]

                required_data = [Stars_names,Distance,Mass,Radius,Lum]
                stars_data.append(required_data)


        headers = ['Stars_names','Distance','Mass','Radius','Lum'] 

        star_df_1 = pd.DataFrame(stars_data,columns = headers)


        star_df_1.to_csv('scraped_data.csv',index=True,index_label='id')               

        #how to create dataframe using pd(pandas) => pd.DataFrame()   
        # 



                        
scrape()    
