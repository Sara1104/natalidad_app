import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def entrenar_modelo():
    df = pd.read_csv("datos/osb_tnatalidad.csv", sep=";")
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df['TOTAL_NACIDOS'] = pd.to_numeric(df['TOTAL_NACIDOS'], errors='coerce')
    df['ANO'] = pd.to_numeric(df['ANO'], errors='coerce')
    datos = df.groupby('ANO')['TOTAL_NACIDOS'].sum().reset_index()

    X = datos[['ANO']]
    y = datos['TOTAL_NACIDOS']
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo, datos

def predecir(modelo, anio):
    anio = np.array([[anio]])
    return int(modelo.predict(anio)[0])
