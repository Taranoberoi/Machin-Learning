import pandas as pd
import numpy as nm
from sklearn import linear_model
import math
from word2number import w2n

df = pd.read_csv("C:\Taran,Courses & others\Machine Leanring Codebasics\Exercise\py-master\ML\linear_reg_multivariate2\Exercise\hiring.csv")
print(df)
# filling Nan with mean value for the column test score and in next line for experience converting it into Zero
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].mean())
df.experience = df.experience.fillna('Zero')

# Converting Float(Actually series) into Int
df['test_score(out of 10)'] = df['test_score(out of 10)'].astype(int)
df.experience = df.experience.apply(w2n.word_to_num)

model = linear_model.LinearRegression()
model.fit(df.drop('salary($)', axis='columns'), df['salary($)'])
print(model.predict([[12,10,10]]))





