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

start = timer() #시작 시간 저장

#파이썬 저장된 폴더내 사용가능, 파일변경 시 파일명 변경
data = pd.read_csv('Merge_File_All.csv' , engine='python', encoding='cp949') #파일 읽기, csv 파일명 변경 필요 ^^ *중요*


print( 'Data 수:',len(data))

print( '\n업종대분류 분포수 :', len( data['상권업종대분류명'].iloc[0:].unique() ))
print( '\n업종대분류 분포 List :', list( data['상권업종대분류명'].iloc[0:].unique() ))

print( '\n업종중분류 분포수 :', len( data['상권업종중분류명'].iloc[0:].unique() ))
print( '\n업종중분류 분포 List :', list( data['상권업종중분류명'].iloc[0:].unique() ))

print( '\n업종소분류 분포수 :', len( data['상권업종소분류명'].iloc[0:].unique() ))
print( '\n업종소분류 분포 List :', list( data['상권업종소분류명'].iloc[0:].unique() ))

end = timer() #종료 시간 저장

print( '실행시간(s) :', timedelta(seconds=end-start))
