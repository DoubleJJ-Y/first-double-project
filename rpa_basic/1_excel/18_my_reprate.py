import pandas as pd

#그냥 csv로하자.
#파일 불러오기
df = pd.read_csv(r'C:\Users\jyjeon_2\Desktop\PY\rpa_basic\WW03_RawData.csv', delimiter=',', encoding='utf-8')

#데이터 필터링
df = df[['CUSTOMER','SCT','SIT','STOPTIME','RT']]
df['WFT'] = df['SCT']+df['SIT']+df['STOPTIME']+df['RT']

#고객으로 그룹화 후 SUM
df2 = df.groupby('CUSTOMER')[['WFT','RT']].sum()

#Reprobing Rate 열 추가
df2['Rep_Rate'] = df2['RT'] / df2['WFT'] *100

#Index 초기화
df2.reset_index(inplace=True)
print(df2.head())

#Excel로 저장
df2.to_excel(
    excel_writer = r'C:\Users\jyjeon_2\Desktop\PY\rpa_basic\Rep_rate.xlsx',
    sheet_name = 'Sheet1',
    index = False       # 0부터 시작하는 자연수 인덱스는 의미가 없음.
    # columns = ['col1, 'col2', 'col3'],
    # na_rep = '',      # 결측값을 ''으로 채우기
    # inf_rep = ''     # 무한값을 ''으로 채우기
)     # 해당 파일이 열려있으면 안됨.

