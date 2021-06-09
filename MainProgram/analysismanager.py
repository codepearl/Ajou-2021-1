########################################################################
#                                                                      #
#   @copyright  Copyright (c) 2021 Pear129, All rights reserved.       #
#   @author     Junyeon-Won                                            #
#   @Ajou       융합시스템공학과 원준연  202020642                     #
#                                                                      #
########################################################################

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import datamanager as dm

manager_name="analysismanager"


def FreqTop(isArea, li): #Freq=빈도, Top=빈도수 상위
    dmdata = dm.DataSearch(isArea, li, manager_name) #scenemanager 에서 입력받은 값을 datamanager 모듈을 통해 필요한 데이터 반환받아 저장
    countsdata=dmdata.value_counts().rename_axis('Red Ocean').reset_index(name='Counts') #Counts 열 추가와 index 재정의
    perdata=(dmdata.value_counts(normalize=True).rename_axis('Red Ocean').reset_index(name='Percentage'))*100 #Percentage 열 추가와 index 재정의
    perdata.drop('Red Ocean',axis=1,inplace=True) #concat을 위해 필요한 열을 남기고 중복되는 열 제거
    perdata=perdata.round(1) #데이터 반올림
    totaldata=pd.concat([countsdata,perdata],axis=1) #Counts와 Percentage 병합
    freqtotal=totaldata.head(15) #상위 15개 데이터 변수에 저장
    return freqtotal

def FreqBottom(isArea, li): #Freq=빈도, Bottom=빈도수 하위
    dmdata = dm.DataSearch(isArea, li, manager_name) #scenemanager 에서 입력받은 값을 datamanager 모듈을 통해 필요한 데이터 반환받아 저장
    countsdata=dmdata.value_counts(ascending=True).rename_axis('Blue Ocean').reset_index(name='Counts') #Counts 열 추가와 index 재정의
    perdata=(dmdata.value_counts(normalize=True,ascending=True).rename_axis('Blue Ocean').reset_index(name='Percentage'))*100 #Percentage 열 추가와 index 재정의
    perdata.drop('Blue Ocean',axis=1,inplace=True) #concat을 위해 필요한 열을 남기고 중복되는 열 제거
    perdata=perdata.round(1) #데이터 반올림
    totaldata=pd.concat([countsdata,perdata],axis=1) #Counts와 Percentage 병합
    freqtotal=totaldata.head(15) #상위 15개 데이터 변수에 저장
    return freqtotal

def WordCloudTop(isArea, li): #빈도수 상위 FreqTop 함수의 'Red Ocean' 데이터를 이용한 WordCloud *값을 반환하지 않고 png 파일을 생성함
    dmdata=FreqTop(isArea,li)
    wcdata=dmdata['Red Ocean']
    wc_all=''
    for i in range(len(wcdata)):
        wc_all=wc_all+wcdata[i]+' '
    wc_all=str(wc_all)  #'Red Ocean' 데이터를 리스트 형태로 한 행마다 저장하여, wordcloud 사용 가능한 데이터로 가공
    wc_gui=WordCloud(width=1000,height=600,background_color="white",random_state=0,font_path=r'c:\windows\Fonts\malgun.ttf')
    wc_gui_show=wc_gui.generate(wc_all)
    wc_gui_show.to_file('graph/wordcloud.png')  #scenemanager 에서 graphmanager와 plot 중복으로 인한 png 형태로 wordcloud를 저장
    plt.axis("off")

def WordCloudBottom(isArea, li): #빈도수 하위 FreqBottom 함수의 'Blue Ocean' 데이터를 이용한 WordCloud *값을 반환하지 않고 png 파일을 생성함
    dmdata=FreqBottom(isArea,li)
    wcdata=dmdata['Blue Ocean']
    wc_all=''
    for i in range(len(wcdata)):
        wc_all=wc_all+wcdata[i]+' '
    wc_all=str(wc_all)  #'Blue Ocean' 데이터를 리스트 형태로 한 행마다 저장하여, wordcloud 사용 가능한 데이터로 가공
    wc_gui=WordCloud(width=1000,height=600,background_color="white",random_state=0,font_path=r'c:\windows\Fonts\malgun.ttf')
    wc_gui_show=wc_gui.generate(wc_all)
    wc_gui_show.to_file('graph/wordcloud.png')  #scenemanager 에서 graphmanager와 plot 중복으로 인한 png 형태로 wordcloud를 저장
    plt.axis("off")
