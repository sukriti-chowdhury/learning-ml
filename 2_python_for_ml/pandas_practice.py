import pandas as pd

# Create a DataFrame with sample dictionary data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
# Display the DataFrame
print("DataFrame:")
print(df)

# Create another series with columns a and b and values as integers, using a dictionary
series_data = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}

series_df = pd.DataFrame(series_data)
# Display the new DataFrame
print("Series DataFrame:")
print(series_df)