#수익률 구하기 여러 종목
import pandas as pd
import numpy as np
from os import name
import FinanceDataReader as fdr

#import dart_fss as dart_fss

import matplotlib.pyplot as plt

#0-0.이곳에 비교할 종목명을 적어주세요!
corp_names = ['태광','성광벤드','하이록코리아']#,'SK하이닉스','NAVER','삼성바이오로직스','삼성전자우','카카오','삼성SDI','현대차']#'LG화학','기아','POSCO홀딩스','KB금융','카카오뱅크','셀트리온','신한지주','삼성물산','현대모비스','SK이노베이션','LG전자','카카오페이','SK','한국전력','크래프톤','하나금융지주','LG생활건강','HMM','삼성생명','하이브','두산중공업','SK텔레콤','삼성전기','SK바이오사이언스','LG','S-Oil','고려아연','KT&G','우리금융지주','대한항공','삼성에스디에스']#'현대중공업','엔씨소프트','삼성화재','아모레퍼시픽','KT','포스코케미칼','넷마블','SK아이이테크놀로지','LG이노텍','기업은행']
#corp_names = ['신세계','현대백화점','호텔신라']
#corp_names = ['LG에너지솔루션','삼성SDI','SK이노베이션','에코프로비엠']


#0.한글폰트 추가
from matplotlib import font_manager as fm
plt.rc('font', family='gulim') # For Windows

#1.한국거래소 Data 가져오기
sf_spx = fdr.StockListing('KRX')
df= sf_spx[['Name','Code']]

#2.Ticker 알기 위한 함수 - 변수:User Input.
def get_cp(corp_name):
    df = pd.DataFrame(sf_spx)
    cond = (df['Name']==f'{corp_name}')
    df = df[cond]
    krx_cp = df[['Code','Name']]
    return krx_cp

#3.다중 기업의 기업명/Ticker 를 각각 Table로 만드는 for문
dfs = []
for corp_name in corp_names:
  try:
    my_df = get_cp(corp_name)
    dfs.append(my_df)
  except: 
    print(f'error-{name}')    

cp_list = pd.concat(dfs)
cn_list = cp_list[['Name']]
cp_list = cp_list[['Code']]  

#4.수익률 차트 그리기 위한 수익률 추출 함수. - 변수:Ticker
def make_rate(code):
  df = fdr.DataReader(code,'2023-01-01') #시작 날짜
  original = df[['Close']].iloc[0] # 첫 번째 값
  df = (df[['Close']] / original - 1)*100
  return df[['Close']]

#5 수익률 추출한 여러 DF를 하나의 DF 로 합쳐서 그래프 그려주는 함수 - 변수:기업명/티커 (*Type : DataFrame)
Stock_cnt = len(cn_list)
def draw_graph(your_name, your_code):
  your_df = pd.DataFrame()
  for i in range(0,Stock_cnt):
    your_df[f'{cn_list.iloc[i,0]}'] = make_rate(f'{cp_list.iloc[i,0]}')
    plt.plot(your_df[f'{cn_list.iloc[i,0]}'],label=f'{cn_list.iloc[i,0]}' )
  plt.xlabel('Date')
  plt.ylabel('수익률')
  plt.legend()
  plt.show()

draw_graph(cn_list,cp_list)
