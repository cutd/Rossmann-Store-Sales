__author__ = 'tgray'
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=list('abcde'), columns=['one','two','three'])

df.ix[1, :-1] = np.nan
df.ix[1:-1, 2] = np.nan

df = df.fillna(0)
print df

