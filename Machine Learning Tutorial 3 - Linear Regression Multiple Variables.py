import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import math # this library gives median value


df = pd.read_csv("C:\Taran,Courses & others\Machine Leanring Codebasics\Exercise\py-master\ML\linear_reg_multivariate2\homeprices.csv")
# print(df)

print(df.bedrooms.median())

df.bedrooms = df.bedrooms.fillna(df.bedrooms.median()) # assign median value to column where there is NaN
print(df)

model = linear_model.LinearRegression()
model.fit(df.drop('price',axis='columns'),df.price)
print(model.predict([[5000,6,8]]))
print(model.coef_)
print(model.intercept_)
