import pandas as pd
import glob

#파일 경로에 있는 csv Merge
#파일 경로 및 저장 위치 실행시 변경 필수

path = r'C:\Users\DY\Downloads\소상공인시장진흥공단_상가(상권)정보_20210331\test\Region_csv'                     # use your path
output_file= r'C:\Users\DY\Downloads\소상공인시장진흥공단_상가(상권)정보_20210331\test\Region_csv\All_Data_File.csv'  # 마지막에 파일 이름
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None,encoding='cp949', dtype='unicode')
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv(output_file, index=False, encoding='cp949')
