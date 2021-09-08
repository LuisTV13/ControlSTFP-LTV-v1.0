from os import sep
import pandas as pd
import numpy as np
from credencial import getColumn

rutadf = 'src/extrac/Ventas.csv'

columnafecha = getColumn('SOFTYS')


df = pd.read_csv(rutadf , header=None ,sep ='|',dtype=np.object0 )
print(df)
k=max(df[int(columnafecha)])

print(k)