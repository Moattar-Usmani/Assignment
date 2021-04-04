#find maximum temperature in MaxTemp column in weather.csv dataset and determined, did it rain that day when MaxTemp was maximum.

# Reading an excel file using Python
import csv
ex= []
main_data = {}
with open('weather.csv','rt') as file:
    weather = csv.reader(file)
    for row in weather:
        main_data[str(row)] = row
maxtemp = []
for column in main_data:
    x = main_data[str(column)][1]
    maxtemp.append(x)
maxtemp.pop(0)
for i in range(0,len(maxtemp)):
    maxtemp[i] = float(maxtemp[i])
print(maxtemp)
max = max(maxtemp)
index = maxtemp.index(max)
index +=1
print("The maxtemp = ",max)
for i in main_data:
    if main_data[i][1] == "35.8":
        print("there is a ran = ",main_data[i][21])








