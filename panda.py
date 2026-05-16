def print_line():
    print("-" * 50)


import pandas as pd

series_1 = [1, 2, 3, 4, 5]
series_2 = [1, 2, 3, 4, 5,"Hello"]

panda_series_1 = pd.Series(series_1)
panda_series_2 = pd.Series(series_2)

print(panda_series_1) # dtype:int64 because it contains only integer values.
print(panda_series_2) # dtype:object because it contains a string value.


print_line()

# Creating a Series with a custom index
custom_index_series = pd.Series(series_1, index=['a', 'b', 'c', 'd', 'e']) # if we add extra index, it will throw an error (IndexError) because the length of the index must match the length of the data.
print(custom_index_series)

print_line()

# Accessing elements in a Series
print(panda_series_1[0]) # Accessing the first element (index 0)
print(panda_series_1[1:4]) # Accessing a range of elements (index 1 to 3)
print(custom_index_series['a']) # Accessing an element using a custom index

print_line()

# Performing operations on Series
print("Result of adding 10 to each element: " + str(panda_series_1 + 10)) # Adding a scalar value to each element in the Series
print("Result of multiplying each element by 2: " + str(panda_series_1 * 2)) # Multiplying each element in the Series by a scalar value
print("Result of adding two Series together: " + str(panda_series_1 + panda_series_1)) # Adding two Series together (element-wise addition)
print("Result of multiplying two Series together: " + str(panda_series_1 * panda_series_1)) # Multiplying two Series together (element-wise multiplication)
print("Mean of the Series: " + str(panda_series_1.mean())) # Calculating the mean of the Series
print("Sum of the Series: " + str(panda_series_1.sum())) # Calculating the sum of the Series
print("Description of the Series: " + str(panda_series_1.describe())) # Generating descriptive statistics for the Series
print("Value counts of the Series: " + str(panda_series_1.value_counts())) # Counting the occurrences of each unique value in the Series
print("Unique values in the Series: " + str(panda_series_1.unique())) # Getting the unique values in the Series
print("Null values in the Series: " + str(panda_series_1.isnull())) # Checking for null values in the Series
print("Non-null values in the Series: " + str(panda_series_1.notnull())) # Checking for non-null values in the Series
print("Sorted values in the Series: " + str(panda_series_1.sort_values())) # Sorting the values in the Series
print("Sorted index of the Series: " + str(panda_series_1.sort_index())) # Sorting the Series by its index

print_line()



# iloc and loc are used for indexing and selecting data in a Series or DataFrame.
print("Using iloc to access the first element: " + str(panda_series_1.iloc[0])) # Accessing the first element using iloc (integer-based indexing)
print("Using iloc to access a range of elements: " + str(panda_series_1.iloc[1:4])) # Accessing a range of elements using iloc (integer-based indexing)
print("Using loc to access an element by index label: " + str(custom_index_series.loc['a'])) # Accessing an element using loc (label-based indexing)
print("Using loc to access a range of elements by index label: " + str(custom_index_series.loc['a':'c'])) # Accessing a range of elements using loc (label-based indexing)

