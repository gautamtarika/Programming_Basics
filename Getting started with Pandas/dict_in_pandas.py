import pandas as pd
subject={ 'Python': [10,20,30],'Java': [15,24,34]}
x=pd.DataFrame(subject,index=['Ajay','Raj','Harsh'])
print(x.loc['Harsh'])