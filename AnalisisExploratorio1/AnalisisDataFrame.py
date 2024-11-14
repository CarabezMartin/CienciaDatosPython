#Importamos la libreria de pandas
import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from docutils.nodes import inline
from scipy.stats import norm
from scipy import stats
import warnings


#Creamos un DataFrame y lo llenamos con el archivo train.csv
df_train = pd.read_csv('C:/Users/jorgeav/Documents/CienciaDatosPython/Recursos/train.csv')
print(df_train['SalePrice'].describe())
sns.histplot(df_train['SalePrice'],kde=True)
plt.show()