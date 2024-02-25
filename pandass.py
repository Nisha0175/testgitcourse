import pandas as pd
'''
data = {
    "id" : [1,2,3],
    "name" : ["m","n","o"]

}
'''
df  = pd.read_csv('data.csv')

print(df.head(10))