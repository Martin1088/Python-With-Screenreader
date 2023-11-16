import pandas as pd
import numpy as np

a = np.array([[2,2,4,2,4],[3,4,4,3,2],[2,4,3,1,2]])
df = pd.DataFrame(data=a)
df = df.T
df = df.rename(columns={0: 'Tim', 1: 'Vallerie', 2: 'Eden' })
df = df.rename(index={0: 'gestern', 1: 'heute', 2: 'morgen', 3: 'über morgen', 4: 'am Ende'})
print(df)

