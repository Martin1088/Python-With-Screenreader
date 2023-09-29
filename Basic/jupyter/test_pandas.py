import pandas as pd
import numpy as np

a = np.array([[2,2,4,2,4],[3,4,4,3,2],[2,4,3,1,2]])
print(a)
print()
df = pd.DataFrame(data=a)
print(df)
print()
df = df.T
print(df)



