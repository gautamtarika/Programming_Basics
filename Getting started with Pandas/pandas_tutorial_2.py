import pandas as pd
import numpy as np

exam_info ={'name':['ajay','raj','harsh','gautam'],'score': [np.NaN, 16, 18, 20],'attempts':[1,2,2,1],'qualify':['no','no','yes','yes']}
df=pd.DataFrame(exam_info)
print(df.info())

print(df.iloc[:2])
print("ONLY NAME AND SCORE")
print(df[['name','score']])
print("SPECIFIC COLUMN")
print(df.iloc[[1,3],[0,2]])
print(df[df['score'].isnull()])
print(df[df['score'].between(16,20)])