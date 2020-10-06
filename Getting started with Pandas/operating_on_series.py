import pandas as pd
ds1 = pd.Series([12, 14, 16, 18, 20, 24])
ds2= pd.Series([2, 4, 6, 8, 10, 12])
print(ds1+ds2)

print(ds1-ds2)

print(ds1*ds2)

print(ds1==ds2)
print(ds1>ds2)
print(ds1<ds2)