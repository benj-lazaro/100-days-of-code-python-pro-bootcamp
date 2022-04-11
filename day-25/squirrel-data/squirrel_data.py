import pandas

# Read the CSV file
data = pandas.read_csv("2018_central_park_squirrel_census_-_squirrel_data.csv")

# Comb through & collect required data
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

# Store collected data to a dictionary
color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Convert dictionary into a Dataframe
squirrel_data = pandas.DataFrame(color_dict)

# Write DataFrame to a .CSV file
squirrel_data.to_csv("squirrel_color_data.csv")
