a=0
b=0

import csv
ex= []
weatherreport = {}
with open('weather.csv','rt') as file:
    weather = csv.reader(file)
    for row in weather:
        weatherreport[str(row)] = row

for i in weatherreport:
    if weatherreport[i][1] > "30":
        if weatherreport[i][21] == "Yes":
            a +=1
        else:
            b +=1

print("(",a," + ",b,")/2")
probability = (a+b)/2
print("the probability of rain: ",probability)
