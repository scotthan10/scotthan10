import pandas as pd
import openpyxl


df1 = pd.read_excel("종목명.xlsx", sheet_name='1')
df2 = pd.read_excel("종목코드_종목명.xlsx", sheet_name='1')


df = pd.merge(df2, df1, how='left' , on='종목코드'). head()

# print(type(df["종목명"]))
print(df)
print(df.iat[2,1])



# print(df["종목명"][0])


