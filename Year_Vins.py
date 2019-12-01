import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel(r"C:\Data Files\Model_Data.xlsx")
print(df)

model = linear_model.LinearRegression()
model.fit(df.drop('COUNT', axis='columns'), df['COUNT'])
print(model.predict([[1,2019]]))
print(model.coef_)


