import requests
import csv
import time
from bs4 import BeautifulSoup

url = 'https://api.wheretheiss.at/v1/satellites/25544'
data = open("ISS_information.csv", "w", newline='')
writer = csv.writer(data)

t0 = time.time()
t1 = t0
n = 1

writer.writerow(["id", "lat", "lng"])

while(True):
    if(t1 - t0 >= 5 * 60):
        print(n)
        response = requests.get(url)
        response.encoding = 'utf-8'

        api = response.text.split(",")


        latitude = api[2].split(":")[1]
        longitude = api[3].split(":")[1]

        info = [n, latitude, longitude]

        writer.writerow(info)
        
        n += 1
        if(n > 18):
            data.close()
            break
        
        t0 = t1
        
    t1 = time.time()