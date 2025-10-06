"""
Write a Python program using Pandas to create a DataFrame from the given data and calculate the monthly average temperature difference between two cities.

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'City_A_Temp': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21],
    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]
}
df = pd.DataFrame(data)
"""

import pandas as pd

data: dict = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'City_A_Temp': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21],
    'City_B_Temp': [10, 12, 15, 17, 20, 22, 25, 24, 20, 18, 14, 11]
}

temparatureDF: pd.DataFrame = pd.DataFrame(data)
temparatureDF['Avg_Temp_Difference'] = temparatureDF['City_A_Temp'] - temparatureDF['City_B_Temp']

print('--------------DF with temperature difference----------------------')
print(temparatureDF)