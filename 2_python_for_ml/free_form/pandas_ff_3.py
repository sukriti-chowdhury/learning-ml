"""
Write a Python program using Pandas to create a DataFrame from the given data and find the total revenue and average price of items sold in each store.
data = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],
    'Price': [50, 20, 30, 60, 55, 22, 33, 65],
    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]
}
"""

import pandas as pd

data: dict = {
    'Store': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Item': ['Apple', 'Banana', 'Orange', 'Grape', 'Apple', 'Banana', 'Orange', 'Grape'],
    'Price': [50, 20, 30, 60, 55, 22, 33, 65],
    'Quantity': [10, 12, 15, 16, 20, 25, 30, 35]
}

itemsDF: pd.DataFrame = pd.DataFrame(data)
itemsDF['Revenue'] = itemsDF['Price'] * itemsDF['Quantity']
print(itemsDF.groupby(by='Store').agg({'Revenue': 'sum', 'Price': 'mean'}).rename(columns={'Price': 'Average Price'}))