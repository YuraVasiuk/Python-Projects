import pandas
import matplotlib.pyplot as plt
import matplotlib

data = pandas.read_csv("data/weather_year.csv")

"""
Getting Started
"""
#print(data)
#print(len(data))
#print(data.columns)

#print(data["EDT"])
#print(data.EDT)

#print(data[["EDT", "Mean TemperatureF"]])

#print(data.EDT.head())
#print(data.EDT.tail(10))
#print(data["EDT"].head(7))
#print(data["Mean TemperatureF"].tail(7))

"""
Fun with Columns
"""

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                 "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                 "min_humidity", "max_pressure", "mean_pressure",
                 "min_pressure", "max_visibilty", "mean_visibility",
                 "min_visibility", "max_wind", "mean_wind", "min_wind",
                 "precipitation", "cloud_cover", "events", "wind_dir"]
#print(data.columns)
#print(data.min_temp.head())
#print(data.min_temp.std())
#print(data.mean_temp.hist())
#print(data.std())

"""
Historying, Plotting
"""
