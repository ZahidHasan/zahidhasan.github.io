---
published: true
key: 10-02-2022
title: Linear Regression with Scikit Learn
tag:
  - Linear Regression
  - Machine Learning
  - Scikit Learn
---
## In previous tutorial we code linear regrassion manually, in this tutorial we will use LinearRegression() function from Scikit-Learn library.

### Importing equired library
```ps
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
```

### Load our simple dataset house price. It has two column area and price and we fit a line to this model.
```ps
df = pd.read_csv('homeprices.csv')
X = df[['area']].values # convert numpy representation. without conversion works but gives warning
#X = pd.DataFrame(df.area) # alternative way to get X
#X = df.iloc[::,0:1:1] # alternative way to get X
#X = df.iloc[:,0] # alternative way to get X
y = df['price'].values  # convert numpy representation. without conversion works but gives warning
#y = df.iloc[::,1:2:1] # alternative way to get y
#y = df.iloc[:,1] # alternative way to get y
plt.scatter(X,y)
#plt.plot(df['area'],df['price'],'r*') # # alternative way to plot
plt.xlabel('area')
plt.ylabel('price')
```
![houseprice.png]({{site.baseurl}}/images/houseprice.png)

Scatter plot will look like

![lr_scatter.png]({{site.baseurl}}/images/lr_scatter.png)

### Ceate mode and fit
```ps
model = LinearRegression()
model.fit(X,y)
```
Our model is created as a line which is best fit for the data points (min error). Now lets predict some price given house area

