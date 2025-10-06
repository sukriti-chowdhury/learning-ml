"""
Write a Python program using Pandas to create a DataFrame from the given data and calculate the total amount spent by each customer.
data = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}
"""

import pandas as pd

data: dict = {
    'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'Item': ['Pen', 'Pencil', 'Notebook', 'Eraser', 'Pen', 'Pencil', 'Notebook', 'Eraser'],
    'Price': [10, 5, 50, 20, 10, 5, 50, 20],
    'Quantity': [3, 4, 2, 5, 10, 6, 1, 2]
}

customerPurchaseDF: pd.DataFrame = pd.DataFrame(data)
customerPurchaseDF['Total'] = customerPurchaseDF['Price'] * customerPurchaseDF['Quantity']
print('------Customer Purchase DataFrame------')
print(customerPurchaseDF)

print('------Result DataFrame------')
totalSpentDF: pd.DataFrame = customerPurchaseDF.groupby(by='Customer').agg({'Total' : 'sum'}).reset_index()
totalSpentDF.rename(columns={'Total': 'Total Amount Spent'}, inplace=True)
print(totalSpentDF)