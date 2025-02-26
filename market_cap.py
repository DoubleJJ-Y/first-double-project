import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
browser.maximize_window()

# 1.페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
url2 = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page='
browser.get(url)

# 2.조회 항목 초기화 (*체크되어 있는 항목 체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():  # 체크된 상태라면?
        checkbox.click() #클릭해서 해제

# 3. 조회 항목 설정 (원하는 항목)
items_to_select = ['영업이익', '자산총계', '매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') #부모 엘리먼트 찾기
    label = parent.find_element(By.TAG_NAME, 'label') #label이라는 TAG Name을 찾아 반환
    print(label.text)
    if label.text in items_to_select: #선택할 항목과 일치 한다면
        checkbox.click() #체크        
        

# 4. 적용하기 버튼 클릭
#btn_apply = browser.find_element(By.XPATH, '//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]') 그냥 개발자도구 XPATH COPY해도 된다.
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]') #XPATH 잡아주기. a tag의 href가 "" 인 거.
btn_apply.click()


for idx in range(1,48) :#1이상 48 미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url+str(idx))

    # 5. Data 추출
    df = pd.read_html(browser.page_source)[1] #df = pd.read_html(url) 도 가능
    #df.head(10)
    df.dropna(axis='index', how='all', inplace=True) #줄 기준, 줄이 모두 결측치일경우 삭제(*all이 아니다 any면 하나라도 결측치일 경우), inplace가 df에 반영
    df.dropna(axis='columns' , how='all', inplace=True) #열 기준
    if len(df) == 0: #더 이상 가져올 data 가 없으면.
        break 

    # 6. 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): #파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False) # encoding 한글파일, mode 'a'는 append인듯.
    else: #파일이 없다면? 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig',index=False)     #header는 자동 포함.
    print(f'{idx} 코스피 페이지 완료')
    time.sleep(1)

#코스닥
for idx in range(1,36) :#1이상 48 미만 페이지 반복
    # 사전 작업 : 페이지 이동
    browser.get(url2+str(idx))

    # 5. Data 추출
    df = pd.read_html(browser.page_source)[1] #df = pd.read_html(url) 도 가능
    #df.head(10)
    df.dropna(axis='index', how='all', inplace=True) #줄 기준, 줄이 모두 결측치일경우 삭제(*all이 아니다 any면 하나라도 결측치일 경우), inplace가 df에 반영
    df.dropna(axis='columns' , how='all', inplace=True) #열 기준
    if len(df) == 0: #더 이상 가져올 data 가 없으면.
        break 

    # 6. 파일 저장
    f_name = 'sise.csv'
    if os.path.exists(f_name): #파일이 있다면? 헤더 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False) # encoding 한글파일, mode 'a'는 append인듯.
    else: #파일이 없다면? 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig',index=False)     #header는 자동 포함.
    print(f'{idx} 코스닥 페이지 완료')
    time.sleep(1)


browser.quit()