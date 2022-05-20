import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('names.csv')  # reads csv file...variable name 'df' can be anything (make sure it is saved in the same folder as you Pycharm project)

print(df)

print(df.loc[[3]])     # print a specific row...you can change '3' for any row

print(df[['Age']])   #print a specific column...you can type the name of a column of your choice

print(df.loc[[4], ['Location']])  # choose a row and a column to print
