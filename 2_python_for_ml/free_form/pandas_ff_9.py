"""
Write a Python program using Pandas to create a DataFrame from the given data and find the total amount spent per item, as well as the total amount spent by all customers.
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

purchaseDF: pd.DataFrame = pd.DataFrame(data)
purchaseDF['Item_Price'] = purchaseDF['Price'] * purchaseDF['Quantity']

print('---------------Purchase DF----------------------')
print(purchaseDF)

# Total amount spent per item
totalAMountByItemDF: pd.DataFrame = purchaseDF.groupby('Item').agg({'Item_Price' : 'sum'}).rename(columns={'Item_Price' : 'Total Price'}).reset_index()
print('---------------Total Amount Per Item DF----------------------')
print(totalAMountByItemDF)

# Total amount spent per customer
totalAMountByCustDF: pd.DataFrame = purchaseDF.groupby('Customer').agg({'Item_Price' : 'sum'}).rename(columns={'Item_Price' : 'Total Amount Spent'}).reset_index()
print('---------------Total Amount Per Customer DF----------------------')
print(totalAMountByCustDF)
