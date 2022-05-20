import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('names.csv')  # reads csv file...variable name 'df' can be anything (make sure it is saved in the same folder as you Pycharm project)


name = input("Enter a Name you want added: ")
age = int(input("Enter the Age you want added: "))
loc = input("Enter the Location you want added: ")
row = 17 + 2


df.loc[row, 'Name'] = name
df.loc[row, 'Age'] = age
df.loc[row, 'Location'] = loc
df.to_csv("names.csv", index=False)
