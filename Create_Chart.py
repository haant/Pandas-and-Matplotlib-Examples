import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('names.csv')  # reads csv file...variable name 'df' can be anything (make sure it is saved in the same folder as you Pycharm project)

df.plot(kind = 'bar', x = 'Name', y = 'Age') # choose the type of graph, choose your x and y labels - 'Kind' can be changed to suite type of chart you want

plt.title('Name and Age')  # add a main title

plt.suptitle('Chart Example')    # add another title above

plt.xlabel('Name')   # add a label to x-axis

plt.ylabel('Age')   # add a label to y-axis

plt.show()      #   show graph
