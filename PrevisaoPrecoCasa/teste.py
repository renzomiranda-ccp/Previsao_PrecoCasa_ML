import pandas as pd
import numpy as np
from sklearn import linear_model


df = pd.read_csv('C:/Users/renzo/OneDrive/Documentos/Dados-Python/PrevisaoPrecoCasa/casas.csv')
print(df)

modelo = linear_model.LinearRegression()
x = df[["area"]]
y = df[["preco"]]
modelo.fit(x,y)

resultado = modelo.predict(pd.DataFrame({"area":[50]}))
valor_arredondado = np.floor(resultado)
