#visualize data
#open csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel = data[data["Primary Fur Color"] == "Gray"]

#grey
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
#red
cinn_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#black
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

#construct data frame as data dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinn_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")