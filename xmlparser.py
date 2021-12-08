# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:35:37 2021

@author: wikara
"""

import pandas as pd # library to handle data in a vectorized manner
import json # library to handle JSON files
import requests # library to handle requests
import folium # map rendering library
import requests
import requests
from bs4 import BeautifulSoup



loc = [51.6238,-0.3049]

Y = str(-0.47012142673841917)
R = str(1200)


for i in range(0, len(loc), 2):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location="+ str(loc[i]) +"%2C"+ str(loc[i + 1])+"&radius="+R+"&type=cafe&key=AIzaSyC4-b_G1DstijLSqu3un_FjWagX9gwZfEM"
    
    51.45241554075301, -0.17156403704199144
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    
    import time
    seconds = time.time()
    secs = round(seconds)
    sstr = str(secs)
    print("Seconds since epoch =", sstr)	
    
    with open('cafe'+ str(loc[i])+ ',' + str(loc[i+1])+'.xml', 'w' , encoding="utf-8") as cfile:
        cfile.write(response.text)
    
    
    infile = open('cafe'+ str(loc[i]) + ',' + str(loc[i+1]) + '.xml', encoding = 'utf8')
    contents = infile.read()
    
    soup = BeautifulSoup(contents, 'xml')
    lats = soup.find_all('location')
    
    Location = [0, ]
    
    for n, lats in enumerate(lats):
        #print(str(lats.text))
        Location.append(str(lats.text))
        
    
    # Writing dataframe to csv
    dataframe = pd.read_xml('cafe'+ str(loc[i])+ ',' + str(loc[i+1])+'.xml')
    
    
    # Dataframe Manipulation starts here
    dataframe['Location'] = Location
    dataframe = dataframe.replace('\n',' ', regex=True)
    LatLong = dataframe["Location"].str.split(" ", expand = True)
    dataframe["Lat"]= LatLong[1]
    dataframe["Long"]= LatLong[2]
    
    dataframe.drop(index=dataframe.index[0], axis=0, inplace=True)
    
    print(dataframe)
    
    #dataframe.to_csv('output.csv')
        