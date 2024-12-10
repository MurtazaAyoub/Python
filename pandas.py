# import pandas as pd
# num = [5, 10, 15, 20, 25]
# series = pd.Series(num)
# print(series + 5) # add 5 to each element
# print(series - 5) # sub 5 to each element
# print(series * 5) # mult 5 to each element
# print(series / 5) # div 5 to each element
# print(series % 5) # show remainder after dividing by 5
# print(Series.Index) #it will print index of elements
# print(Series.tail(3)) #it will print last three elements of an array
# print(Series.head(3)) #it will print first three elements of an array
# print(Series.sum()) # it will add elements

import pandas as pd
data = pd.Series([1, 2, 3, 4, 5])
series = pd.Series(data, index = ('A','B','C','D'))
print(series)
print(series[0:3])
print(series['A':'B'])