import pandas as pd
import FinanceDataReader as fdr
import time
from slacker import Slacker



def assist_index(code):
    
    df = fdr.DataReader(code, '2022-01-01')

    ndays_high = df["High"].rolling(window=5, min_periods=1).max()
    ndays_low = df["Low"].rolling(window=5, min_periods=1).min()
    fast_k = (df["Close"] - ndays_low) / (ndays_high - ndays_low) * 100
    sto_1 = fast_k.ewm(span=3).mean()
    sto_1d = sto_1.ewm(span=3).mean()

    ndays_high = df["High"].rolling(window=10, min_periods=1).max()
    ndays_low = df["Low"].rolling(window=10, min_periods=1).min()
    fast_k = (df["Close"] - ndays_low) / (ndays_high - ndays_low) * 100
    sto_2 = fast_k.ewm(span=6).mean()
    sto_2d = sto_2.ewm(span=6).mean()

    ndays_high = df["High"].rolling(window=15, min_periods=1).max()
    ndays_low = df["Low"].rolling(window=15, min_periods=1).min()
    fast_k = (df["Close"] - ndays_low) / (ndays_high - ndays_low) * 100
    sto_3 = fast_k.ewm(span=9).mean()
    sto_3d = sto_3.ewm(span=9).mean()

    ndays_high = df["High"].rolling(window=20, min_periods=1).max()
    ndays_low = df["Low"].rolling(window=20, min_periods=1).min()
    fast_k = (df["Close"] - ndays_low) / (ndays_high - ndays_low) * 100
    sto_4 = fast_k.ewm(span=12).mean()
    sto_4d = sto_4.ewm(span=12).mean()

    sma_5 = df["Close"].rolling(5).mean()
    sma_10 = df["Close"].rolling(10).mean()
    sma_20 = df["Close"].rolling(20).mean()
    sma_50 = df["Close"].rolling(50).mean()
    

    ewm_100 = df["Close"].ewm(100).mean()
    ewm_200 = df["Close"].ewm(200).mean()
    
    vsma_5 = df["Volume"].rolling(5).mean()
    vsma_20 = df["Volume"].rolling(20).mean()
    
    
    df2 = df.assign(code=str(code), sto_1=sto_1, sto_1d=sto_1d, sto_2=sto_2, sto_2d=sto_2d, sto_3=sto_3,sto_3d=sto_3d, sto_4=sto_4, sto_4d=sto_4d,\
        sma_5 = sma_5,sma_10 = sma_10,sma_20 = sma_20, sma_50 = sma_50, ewm_100=ewm_100,ewm_200=ewm_200,vsma_5=vsma_5,vsma_20=vsma_20 ).dropna()

    df = df2[['code', 'Open', 'High', 'Low', 'Close',  'Volume', 'sto_1','sto_1d', 'sto_2', 'sto_2d', 'sto_3', 'sto_3d', 'sto_4', 'sto_4d',\
        'sma_5', 'sma_10','sma_20','sma_50','ewm_100','ewm_200','vsma_5','vsma_20' ]]
      
    price = df["Close"][-1]
    
    up_trend_0 = sto_1[-1] > sto_1[-2] and sto_2[-1] > sto_2[-2] and sto_3[-1] > sto_3[-2] and sto_4[-1] > sto_4[-2]
        
    up_trend_1 = sto_1[-1] > sto_1[-2]
    up_trend_2 = sto_2[-1] > sto_2[-2]
    up_trend_3 = sto_3[-1] > sto_3[-2]
    up_trend_4 = sto_4[-1] > sto_4[-2]

    
    
    sto_1_gc = sto_1[-1] > sto_1d[-1]
    sto_2_gc = sto_2[-1] > sto_2d[-1]
    sto_3_gc = sto_3[-1] > sto_3d[-1]
    sto_4_gc = sto_4[-1] > sto_4d[-1]
    
    sto_0_gc = sto_1_gc and sto_2_gc and sto_3_gc and sto_4_gc
    
    reqular_arrangement_0 = sto_1[-1] > sto_2[-1] > sto_3[-1]

    reqular_arrangement_1 = sto_1[-1] > sto_2[-1]
    reqular_arrangement_2 = sto_2[-1] > sto_3[-1]
    reqular_arrangement_3 = sto_3[-1] > sto_4[-1]

    volume_rereqular_arrangement_0 = vsma_5[-1] > vsma_20[-1]
    
    sma_rereqular_arrangement_0 = sma_5[-1] > sma_20[-1]
    sma_rereqular_arrangement_1 = sma_20[-1] > sma_50[-1]
    ewm_rereqular_arrangement_0 = ewm_100[-1] > ewm_200[-1]
    ewm_up_trend_0 = ewm_100[-1] > ewm_100[-2]

    
    
    return df, up_trend_0, reqular_arrangement_0, volume_rereqular_arrangement_0,\
        sto_1[-1],sto_2[-1],sto_3[-1],sto_4[-1], \
        sto_1[-2],sto_2[-2],sto_3[-2],sto_4[-2],\
        up_trend_1, up_trend_2, up_trend_3, up_trend_4, \
        sto_0_gc, sto_1_gc, sto_2_gc, sto_3_gc, sto_4_gc, \
        reqular_arrangement_1, reqular_arrangement_2, reqular_arrangement_3,\
        sma_rereqular_arrangement_0, sma_rereqular_arrangement_1, ewm_rereqular_arrangement_0, ewm_up_trend_0,\
        price  
        # 0~3 / 2~5 / 6~9 / 10~14 / 15~19 / 20~23 / 24 / 25~28 / 29


# csv_df = pd.read_csv('SC_220721.csv', encoding='CP949')
# symbol_array = csv_df['Symbol'].values
# symbol_list = symbol_array.tolist()

symbol_list = ['005930', '000660']
searched_list = []

for sym in symbol_list:

    index = assist_index(sym) # 함수 리턴값은 튜플 자료형
    
        
    if index[1] and index[2] and index[3]:
    
        
        code_list = searched_list.append[sym]
        slack = Slacker("xoxb-1534072318850-1585261685223-RH9tHMf4JO6c6ONqmyPZydJY")
        slack.chat.post_message("#주식투자", code_list)
        
        
        print(index[-1])
        
    else:

        df_2 = pd.read_excel("종목코드_종목명.xlsx", sheet_name='1')                
        df_3 = pd.merge(index[0],df_2,how='left',left_on='code', right_on="종목코드").drop("종목코드",axis=1)
        df = df_3[['code', '종목명', 'Open', 'High', 'Low', 'Close',  'Volume', 'sto_1','sto_1d', 'sto_2', 'sto_2d', 'sto_3', 'sto_3d', 'sto_4', 'sto_4d',\
        'sma_5', 'sma_10','sma_20','sma_50','ewm_100','ewm_200','vsma_5','vsma_20' ]]
        
        # code_list = searched_list.append[sym]
        slack = Slacker("xoxb-1534072318850-1585261685223-RH9tHMf4JO6c6ONqmyPZydJY")
        # slack.chat.post_message("#주식투자", df.iat[0,1]) # 종목명
        # slack.chat.post_message("#주식투자", index[-1]) # 현재가
        
        slack.chat.post_message("#주식투자", f"종목코드: {sym} 종목명: {df.iat[0,1]} 현재가: {index[-1]} ")
        
        # print(df.tail())
               

        # print(tuple[1],tuple[2],tuple[3],tuple[-1])
        


