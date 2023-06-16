import pandas as pd

df1 = pd.read_csv('Project128.csv')

df1 = df1.dropna()
#print(type(df1['Mass'].iloc[0]))
# print(type(df1['Radius'].iloc[0]))

print(df1.info())


df1['Mass']=df1['Mass'].astype('float')
df1['Radius']=df1['Radius'].astype('float')

# print(type(df1['Mass'].iloc[0]))
# print(type(df1['Radius'].iloc[0]))

df1['Mass'] = df1['Mass']*0.000954588
df1['Radius'] = df1['Radius']*0.102763

df1.to_csv('Project129Part1.csv')

