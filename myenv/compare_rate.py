#수익률 구하기 여러 종목
import pandas as pd
import numpy as np
from os import name
import FinanceDataReader as fdr

#import dart_fss as dart_fss

import matplotlib.pyplot as plt

#0.한글폰트 추가
from matplotlib import font_manager as fm
plt.rc('font', family='gulim') # For Windows

#df = fdr.DataReader('KRX: 373220','2023')

#1.수익률 비교 함수
def make_rate(code):
  df = fdr.DataReader(code,'2024')
  original = df[['Close']].iloc[0] # 첫 번째 값
  df = (df[['Close']] / original - 1)*100
  return df['Close']


#2.Dart API 받기 & 모든 상장회사 ticker 받기(*Dart)
#api_key = 'ad2deb322980b151b3c81930365990a1736f7fc1'
#dart_fss.set_api_key(api_key=api_key)
#all = dart_fss.api.filings.get_corp_code()
#df_lc = pd.DataFrame(all)  #Table화.
#df_listed = df_lc[df_lc['stock_code'].notnull()] #상장 회사

#2.한국거래소 상장기업 list 받기
sf_krx = fdr.StockListing('KRX')

#3.기업명 -> Corp code 받는 함수
def get_cp(corp_name):
    sf_krx[sf_krx['Name']==f'{corp_name}']


your_df = pd.DataFrame()
your_df['LG엔솔'] = make_rate('373220') #LG엔솔 3
your_df['하닉'] = make_rate('KRX: 000660') #하닉 2
your_df['삼전'] = make_rate('KRX: 005930') #삼전 1
your_df['현차'] = make_rate('KRX: 005380') #현차 4
your_df['삼바'] = make_rate('KRX: 207940') #삼바 5

column_names = list(your_df)

plt.plot(your_df[f'{column_names[1]}'], label = f'{column_names[1]}')
plt.plot(your_df[f'{column_names[2]}'], label = f'{column_names[2]}')
plt.xlabel('Date')
plt.ylabel('수익률')
plt.show()
#df.plot()
#df