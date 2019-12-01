import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_csv("C:\Taran,Courses & others\Machine Leanring Codebasics\Exercise\py-master\ML\linear_reg\Exercise\canada_per_capita_income.csv")

print(df)
# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.scatter(df.Area,df.Price,color='red',marker='*')
# plt.show()

# Added new dataframe with same data which imported in the beginning but just dropped Price column
# new_df = df.drop('Price',axis='columns')
# print(new_df)
#
model = linear_model.LinearRegression()
model.fit(new_df,df.Price)
print(model.predict([[10000]]))
print(model.coef_)
print(model.intercept_)