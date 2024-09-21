import pandas as pd

path = "life-expectancy-unwpp.csv"
df = pd.read_csv(path)
df_new = df.loc[df.groupby('Entity')['Year'].idxmax()]
print(df_new.head(29))
df_new.to_csv('life-expectancy-2023.csv', index=False)

