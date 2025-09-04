import pandas as pd
# data = [1, 2, 3, 4, 5]
# data2 = [6, 7, 8, 9, 10]
# series = pd.Series(data)
# series2 = pd.Series(data2)
# series3 = series + series2
# print("Addition:", series3)
# series3 = series - series2
# print("Subtraction:", series3)
# series3 = series * series2
# print("Multiplication:", series3)
# series3 = series / series2
# print("Division:", series3)



# d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# series = pd.Series(d1)
# print("Original dictionary:")
# print(d1)
# print("Converted to Pandas Series:")
# print(series)


# import numpy as np
# list1 = [10, 20, 30, 40]
# series = pd.Series(list1)
# array = np.array([100, 200, 300, 400])
# series1 = pd.Series(array)
# d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# series2 = pd.Series(d1)
# print("Series from list:\n", series)
# print("\nSeries from array:\n", series1)
# print("\nSeries from dictionary:\n", series2)


s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
vertical = pd.concat([s1, s2])
print("Vertical Stack:\n", vertical)
horizontal = pd.concat([s1, s2], axis=1)
print("\nHorizontal Stack:\n", horizontal)