import pandas as pd
import numpy as np

test = np.array([ [4, 6, 4], [1,4,7], [8,4,8] ,[34,4,8], [8,4,12] ] )
df = pd.DataFrame(data=test)
df = df.T
print(df)

