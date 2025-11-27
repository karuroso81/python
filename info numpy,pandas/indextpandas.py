import pandas as pd
print( pd.__version__)

serie1 = pd.Series([10, 20, 30, 40])
print("Serie 1:\n", serie1)
serie1.name="primeros"
print("Serie 1:\n", serie1)

df1 = pd.DataFrame({"columna1": [1, 2, 3], "columna2": [4, 5, 6],"columna3": [7, 8, 9]})
print("DataFrame 1:\n", df1)
df1.index = ['a', 'b', 'c']
print("DataFrame 1 con nuevo índice:\n", df1)

df2 = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')
print (df2.head())

print(df2.size)

print(df2.shape)

print(df2.columns)

print(df2.index)
print(df2.tail(3))

df2.columns = ['largo_sepalo', 'ancho_sepalo', 'largo_petalos', 'ancho_petalos', 'especie']
print(df2.head())

df2.iloc[0:5, 0:2] = 0
print(df2.head())

df2.describe()

print(df2['especie'].value_counts())
[df2['especie'] == 'setosa']

df2.memory_usage(deep=True)
print(df2.memory_usage(deep=True))

df1.info()
df2.info()
df2.info(memory_usage='deep')
df2.dtypes
print(df2.dtypes)



df2['largo_sepalo'] = df2['largo_sepalo'].astype('float32')
