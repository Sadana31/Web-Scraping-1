# importing necessary modules
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv
import numpy as np

# getting data from URL
page = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")

# getting text and finding table using modules
soup = bs(page.text,'html.parser')
info_table_star = soup.find('table')

# empty array
temp_list= []
# finding table rows with <tr> tag (table row)
table_data = info_table_star.find_all('tr')


# initializing the array to add data respectively
name_of_star = []
distance_from_earth =[]
Mass = []
Radius =[]
Lum = []

#getting data from row using <td> tag (table data)
for tr in table_data:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# specifying data
headers = ["name_of_star" , "distance_from_earth" , "Mass" , "Radius" , "Lum"]

# looping through  table data and adding data accordingly
for i in range(1,len(temp_list)):
    name_of_star.append(temp_list[i][1])
    distance_from_earth.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

# creating csv filr using pd.DataFrama about stars' DataFrama
# I HAD TO BREAK MY HEAD ON HOW TO DO THIS SINCE csvwriter wouldn't work😣😣
stars_info = pd.DataFrame(list(zip(name_of_star,distance_from_earth,Mass,Radius,Lum)),
columns=['Star_name','distance_from_earth','Mass','Radius','Luminosity'])

stars_info.to_csv('stars.csv')

# creating separate files for individual data for other purposes
stars_name = pd.DataFrame(list(name_of_star),columns=["Star_name"])
stars_name.to_csv("names.csv")

stars_name = pd.DataFrame(list(distance_from_earth),columns=["distance_from_earth"])
stars_name.to_csv("distance.csv")




