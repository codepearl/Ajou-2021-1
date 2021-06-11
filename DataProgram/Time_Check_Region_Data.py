########################################################################
#                                                                      #
#   @copyright  Copyright (c) 2021 Pear129, All rights reserved.       #
#   @author     GuDY                                                   #
#   @Ajou       융합시스템공학과 구동용  202020636                         #
#                                                                      #
########################################################################

import pandas as pd
from timeit import default_timer as timer
from datetime import timedelta
#파이썬 저장된 파일에서 각 지역별 파일 있으면 실행가능

#강원
start0 = timer() #시작 시간 저장
data0 = pd.read_csv('강원.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data0))

end0 = timer() #종료 시간 저장

print( '강원 실행시간 :', timedelta(seconds=end0-start0))


#경기
start1 = timer() #시작 시간 저장
data1 = pd.read_csv('경기.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data1))

end1 = timer() #종료 시간 저장

print( '경기 실행시간 :', timedelta(seconds=end1-start1))


#경남
start2 = timer() #시작 시간 저장
data2 = pd.read_csv('경남.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data2))

end2 = timer() #종료 시간 저장

print( '경남 실행시간 :', timedelta(seconds=end2-start2))


#경북
start3 = timer() #시작 시간 저장
data3 = pd.read_csv('경북.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data3))

end3 = timer() #종료 시간 저장

print( '경북 실행시간 :', timedelta(seconds=end3-start3))


#광주
start4 = timer() #시작 시간 저장
data4 = pd.read_csv('광주.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data4))

end4 = timer() #종료 시간 저장

print( '광주 실행시간 :', timedelta(seconds=end4-start4))


#대구
start5 = timer() #시작 시간 저장
data5 = pd.read_csv('광주.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data5))

end5 = timer() #종료 시간 저장

print( '대구 실행시간 :', timedelta(seconds=end5-start5))


#대전
start6 = timer() #시작 시간 저장
data6 = pd.read_csv('대전.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data6))

end6 = timer() #종료 시간 저장

print( '대전 실행시간 :', timedelta(seconds=end6-start6))


#부산
start7 = timer() #시작 시간 저장
data7 = pd.read_csv('부산.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data7))

end7 = timer() #종료 시간 저장

print( '부산 실행시간 :', timedelta(seconds=end7-start7))


#서울
start8 = timer() #시작 시간 저장
data8 = pd.read_csv('서울.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data8))

end8 = timer() #종료 시간 저장

print( '서울 실행시간 :', timedelta(seconds=end8-start8))


#세종
start9 = timer() #시작 시간 저장
data9 = pd.read_csv('세종.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data9))

end9 = timer() #종료 시간 저장

print( '세종 실행시간 :', timedelta(seconds=end9-start9))


#울산
start10 = timer() #시작 시간 저장
data10 = pd.read_csv('울산.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data10))

end10 = timer() #종료 시간 저장

print( '울산 실행시간 :', timedelta(seconds=end10-start10))


#인천
start11 = timer() #시작 시간 저장
data11 = pd.read_csv('인천.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data11))

end11 = timer() #종료 시간 저장

print( '인천 실행시간 :', timedelta(seconds=end11-start11))


#전남
start12 = timer() #시작 시간 저장
data12 = pd.read_csv('전남.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data12))

end12 = timer() #종료 시간 저장

print( '전남 실행시간 :', timedelta(seconds=end12-start12))


#전북
start13 = timer() #시작 시간 저장
data13 = pd.read_csv('전북.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data13))

end13 = timer() #종료 시간 저장

print( '전북 실행시간 :', timedelta(seconds=end13-start13))


#제주
start14 = timer() #시작 시간 저장
data14 = pd.read_csv('제주.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data14))

end14 = timer() #종료 시간 저장

print( '제주 실행시간 :', timedelta(seconds=end14-start14))


#충남
start15 = timer() #시작 시간 저장
data15 = pd.read_csv('충남.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data15))

end15 = timer() #종료 시간 저장

print( '충남 실행시간 :', timedelta(seconds=end15-start15))


#충북
start16 = timer() #시작 시간 저장
data16 = pd.read_csv('충북.csv' , engine='python', encoding='cp949') #파일 읽기

print( 'Data 수:',len(data16))

end16 = timer() #종료 시간 저장

print( '충북 실행시간 :', timedelta(seconds=end16-start16))
