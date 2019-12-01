import pandas as pd
import numpy as nm
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("C:\Taran,Courses & others\Machine Leanring Codebasics\Exercise\py-master\ML\linear_reg\Exercise\canada_per_capita_income.csv")
# print(df)

# plt.xlabel('year')
# plt.ylabel('Income')
# plt.scatter(df.year,df.Income,color='purple',marker="+")
# plt.show()

new_df = df.drop('Income',axis='columns')
#print(new_df)

model =linear_model.LinearRegression()
model.fit(new_df,df)
# print(model.predict([[2020]]))

print(model.coef_)
#print("Model predicted INtercept value is",model.intercept_)


