import pandas as pd
import numpy as np

a = np.array([[2,2,4,2,4],[3,4,4,3,2],[2,4,3,1,2]])
df = pd.DataFrame(data=a)
df = df.T
df = df.rename(columns={0: 'BFK', 1: "PK", 2: 'GK'})
df = df.rename(index={0: 'Mertens', 1: 'Schlütter', 2: 'Andlauer', 3: 'Fechner', 4: 'Ruhl'})
print(df)
df = df.drop(columns='GK')
df = df.drop(columns='GK')
df = df /2
df.BFK = df.BFK.map({1.0: 'sehr gut',  1.5: 'gut', 2.0: 'gut'})
df.PK = df.PK.map({1.0: 'sehr gut', 1.5: 'gut' , 2.0: 'gut'})
print(df)

