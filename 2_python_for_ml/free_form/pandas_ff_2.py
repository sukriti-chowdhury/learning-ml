"""
Given the following DataFrame, write a Python program using Pandas to extract all rows where the price is greater than or equal to 20,000 and sort them in descending order by price.
data = {
    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],
    'Price': [25000, 12000, 8000, 22000, 5000]
}
"""

import pandas as pd

data: dict = {
    'Product': ['Laptop', 'Desktop', 'Tablet', 'Phone', 'Smartwatch'],
    'Price': [25000, 12000, 8000, 22000, 5000]
}

productDF: pd.DataFrame = pd.DataFrame(data)
productGT20000DF: pd.DataFrame = productDF[productDF['Price'] >= 20000]
print(productGT20000DF.sort_values(by='Price', ascending=False))