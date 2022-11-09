# learning PANDAS
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines() #take each line in file into an item in list
#     print(data)
# #add each line into a list
# data = []

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) #reads in each item as a single value
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)
#

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) can be series and data frames

data_dict = data.to_dict() #convert each column to a dictionary
temp_list = data["temp"].to_list() #turns data series into python list

#average temp
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)
#easier method
print(data["temp"].mean())

#find maximum temp value
print(data["temp"].max())

#get data in columns
condition_list = data.condition #calls condition column

#get data in rows
#get hold of entire row where day is monday
monday_list = data[data.day == "Monday"]


#pull out row of data where temp is at maximum
max_temp = data[data.temp == data.temp.max()]

#select mondays temperature in farenheight
monday = data[data.day == "Monday"]
temp_f = int(monday.temp * 9/5 + 32)
print(temp_f)

#create a data frame from scratch
data_dict = {
    "students": ["amelia", "sidney"],
    "scores": [100, 100]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("mydataa.csv")