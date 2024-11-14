#Importamos la libreria de pandas
import pandas as pd

#Creamos un DataFrame y lo llenamos con el archivo train.csv
df_train = pd.read_csv('C:/Users/jorgeav/Documents/CienciaDatosPython/Recursos/train.csv')
#La función HEAD solo me trae la cantidad de filas que se le especifique en este caso son 20
print(df_train.head(20))
#La función SHAPE me da las dimenciones del DataFrame (filas x columnas)
print(df_train.shape)
#Con los [] se especifica que columna seleccionamos
print(df_train['Id'])
#Muestra el valor medio de la columna SalePrice con la funcion MEAN
print("Promedio de la columna SalePrice: ", df_train['SalePrice'].mean())
print(df_train.describe())