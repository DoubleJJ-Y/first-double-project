import os, time
import pyautogui
from PIL import ImageChops

#위쪽(원본) 이미지의 시작점 (# width 528, # Height 423)
#675,41 #1203,41 #675,464 #1203,464

#아래쪽 이미지의 시작점 (# width 528, # Height 423)
#675,469 #1203,469 #675,892 #1203,892

#1203-675 = 528 / 892-469 = 423
width, height = 528, 423
y_pos_org = 41
x_pos = 675

y_pos_dif = 469



src = pyautogui.screenshot(region = (x_pos, y_pos_org, width, height))
dest = pyautogui.screenshot(region = (x_pos, y_pos_dif, width, height))

src.save('src.jpg')
dest.save('dest.jpg')

diff = ImageChops.difference(src, dest)
diff.save('diff.jpg')

#파일 생성 대기 
while not os.path.exists('diff.jpg'):
        time.sleep(1)

import cv2
src_img = cv2.imread('src.jpg')
dest_img = cv2.imread('dest.jpg')
diff_img = cv2.imread('diff.jpg')

#Gray 화 후 외곽선 찾기
gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY) #BGR을 GRAY로 바꿈. CV는 보통 RGB라고 부르지 않음.
#gray = (gray > 25) * gray # threshold 주기

contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
#EXTERNAL - 외곽선의 가장 바깥부분
#CHANIN_APPROX_NONE 모든 외곽선을 표시

COLOR = (0, 200, 0)
for cnt in contours:
    #if cv2.contourArea(cnt) > 10:
    x, y, width, height = cv2.boundingRect(cnt) #외곽선을 감싸는 사각형
    #사각형을 그리는데, src_image에 위에서 받아온 크기 정보에 COLOR색으로 굵기는2
    cv2.rectangle(src_img, (x,y), (x + width, y + height), COLOR, 2) 
    cv2.rectangle(dest_img, (x,y), (x + width, y + height), COLOR, 2) 
    cv2.rectangle(diff_img, (x,y), (x + width, y + height), COLOR, 2) 
    
    # #마우스 이동 및 클릭
    # to_x = x+(width // 2) 
    # to_y = y+(width // 2) + y_pos_org
    # pyautogui.moveTo(to_x, to_y, duration=1)  #사실 moveTo는 필요없이 클릭만해도된다.
    # pyautogui.Click(to_x, to_y)
    # time.sleep(1)

cv2.imshow('src', src_img)
cv2.imshow('dest', dest_img)
cv2.imshow('diff', diff_img)

cv2.waitKey(0) #아무키 누를때까지 0(무한) 대기
cv2.destroyAllWindows()


# result = pyautogui.confirm('틀린 그림 찾기', bottons = ['시작', '종료'])
# if result == '종료':
#     print('종료') #프로그램 종료

