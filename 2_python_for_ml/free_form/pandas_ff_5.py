"""
Write a Python program using Pandas to create a DataFrame from the given data and find the month with the highest average temperature.
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]
}
df = pd.DataFrame(data)
"""

import pandas as pd

data: dict = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [20, 22, 25, 27, 30, 32, 35, 34, 30, 28, 24, 21]
}

tempDF: pd.DataFrame = pd.DataFrame(data)
max_temp: int = tempDF['Temperature'].max()
warmest_month: str = tempDF[tempDF['Temperature'] == max_temp]['Month'].values[0]
print(f"The month with the highest average temperature is {warmest_month} with a temperature of {max_temp}°C.")