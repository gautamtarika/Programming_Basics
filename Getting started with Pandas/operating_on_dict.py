import pandas as pd
import numpy as np

exam_info = {'name': ['ajay', 'raj', 'harsh', 'gautam'], 'score': [
    np.NaN, 16, 18, 20], 'attempts': [1, 2, 2, 1], 'qualify': ['no', 'no', 'yes', 'yes']}
df = pd.DataFrame(exam_info)

df.loc[0,'score']=16
#adding new row
df.loc[4]=['suresh',18,3,'yes']
print(df)
print("The total attempts are:-",df['attempts'].sum())
df['qualify']=df['qualify'].map({'yes':True,'no':False})
df=df.drop(1)
df['name']=df['name'].replace('suresh','ajay')
print(df)
print("Deleting 'Attempts' Column")
df.pop('attempts')
print(df)