import pandas as pd

data = pd.read_csv('전국통합_Header해결함.csv' , engine='python', encoding='cp949')

print(len(data.index[(data['상권업종대분류명'] == '숙박')])) #39234개
print(len(data.index[(data['상권업종대분류명'] == '소매')])) #702607개
print(len(data.index[(data['상권업종대분류명'] == '음식')])) #849967개
print(len(data.index[(data['상권업종대분류명'] == '학문/교육')])) #160257개
print(len(data.index[(data['상권업종대분류명'] == '생활서비스')])) #364938개
print(len(data.index[(data['상권업종대분류명'] == '부동산')])) #74684개
print(len(data.index[(data['상권업종대분류명'] == '관광/여가/오락')])) #48838개
print(len(data.index[(data['상권업종대분류명'] == '스포츠')])) #4452개
