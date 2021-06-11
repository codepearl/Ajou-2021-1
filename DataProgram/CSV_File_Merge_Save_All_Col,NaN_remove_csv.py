########################################################################
#                                                                      #
#   @copyright  Copyright (c) 2021 Pear129, All rights reserved.       #
#   @author     GuDY                                                   #
#   @Ajou       융합시스템공학과 구동용  202020636                         #
#                                                                      #
########################################################################

# 파일 경로내에 있는 모든 csv 파일 통합

import pandas as pd
import glob

#파일 경로와 저장 위치 및 파일명 변경 해야함.
path = r'C:\Users\DY\Downloads\소상공인시장진흥공단_상가(상권)정보_20210331\test\Merge.py'   # use your path
output_file= r'C:\Users\DY\Downloads\소상공인시장진흥공단_상가(상권)정보_20210331\test\Merge.py\MergeFile.csv' # 마지막 저장될 파일 이름
all_files = glob.glob(path + "/*.csv")

li = []

#drop line에서 list에 필요없는 Header 이름쓰면 Columm 제거
for filename in all_files:
    df = pd.read_csv(filename, index_col=None,encoding='cp949', dtype='unicode')
    df.drop(['상가업소번호','상권업종대분류코드','행정동명','상권업종중분류코드',
             '상권업종소분류코드','표준산업분류코드','표준산업분류명','시도코드',
             '시도명','시군구코드','행정동코드','법정동코드','PNU코드','대지구분코드',
             '대지구분명','지번본번지','지번부번지','지번주소','도로명코드','도로명',
             '건물본번지','건물부번지','건물관리번호','건물명','도로명주소','구우편번호',
             '신우편번호','동정보','층정보','호정보','전화번호','상권번호','데이터기준일자'],inplace=True, axis=1) #필요없는 행 제거
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.dropna(subset=['상호명','상권업종대분류명','상권업종중분류명',
                     '상권업종소분류명','시군구명','법정동명','경도','위도'], inplace=True) # 지정한 열에 빈 행 제거
frame.to_csv(output_file, index=False, encoding='cp949')
