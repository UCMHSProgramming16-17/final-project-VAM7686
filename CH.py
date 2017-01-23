#import module
import requests
import csv
import math

#create file
csvfile = open('file.csv', 'w')

#create csv writer
csvwriter = csv.writer(csvfile, delimiter = ',')
 
#write information
csvwriter.writerow(['Date', 'Temperature'])

# Import requests
import requests
import json

url = "https://maps.googleapis.com/maps/api/geocode/json"
key = 'AIzaSyAwPHH9ZDTZHdkXRAPp-CI59U23S9OhSPY'
address = input("Enter an address")
payload = {'key':'', 'address': address}

# Make a request
r = requests.get(url, params=payload)
#print(r.url)
#process data
data = r.json()
#print(data)
location = data['results'][0]
geometry = location['geometry']['location']
#print(location.keys())
print("You are at %s." % location['formatted_address'])
print("Your latitiude is %s and your longitude is %s." % (geometry['lat'], geometry['lng']))

lat = str(geometry['lat'])
lon = str(geometry['lng'])

#creating url for requests

endpoint = 'https://api.darksky.net/forecast/'
key1 = '251cb187f7056e08ba336253030a291a'
payload1 = {'units': 'us'}
YYYY = int(input("pick a year"))

for YYYY in range(YYYY-30, YYYY):

    time = str(YYYY)+"-02-22T24:00:00Z"

    # Assemble full url
    url1 = endpoint + key1 + '/' + lat + ',' + lon + ',' + time
    
    # Make a request
    r1 = requests.get(url1, params=payload1)

    # deal with the information
    weather = r1.json()
    
    for x in range(0, 23):
        hour = weather['hourly']['data'][x]['time']
        print(hour)
        Temperature = weather['hourly']['data'][x]['temperature']
        #Time = hour['time']
        csvwriter.writerow([hour, Temperature])
#close writer
csvfile.close()

#Plotting data points
import bokeh

import pandas as pd

from bokeh.charts import Scatter, output_file, save
from bokeh.charts import HeatMap, output_file, save

#read file
df = pd.read_csv('file.csv')

#Plots a heatmap
p = HeatMap(df, x='Date', y='Temperature', values=None, stat='count', xgrid=False, ygrid=False, hover_tool=True, hover_text=None)

output_file('HeatMap.html')

#Saves graph
save(p)

#box = BoxPlot(df, values='Temperature', label='Date', title="Temperature Date Box Plot", plot_width=400)

#Creates a Scatter Plot
v = Scatter(df, x='Date', y='Temperature', color='red', title="Date vs. Temperature", legend='top_right', xlabel="Date", ylabel="Temperature")

output_file('Scatter.html')

#Saves Graph as a html file
save(v)