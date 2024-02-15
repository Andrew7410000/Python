import numpy as np
import pandas as pd

name = pd.Series(['Example1', 'Example2', 'Example3'])
city = pd.Series(['Example4', 'Example5', 'Example6'])
lines = pd.Series([4, 5, 1])
lon = pd.Series([34.798443, 34.812831, 35.011635])
lat = pd.Series([31.243288, 31.260284, 31.068616])
d = {'name': name, 'city': city, 'lines': lines, 'lon': lon, 'lat': lat}
stations = pd.DataFrame(d)

stations
