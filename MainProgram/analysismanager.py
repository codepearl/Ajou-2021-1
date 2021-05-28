import pandas as pd
import datamanager as dm
import numpy as np

manager_name="analysismanager"

def Recommend(isArea, li):
    dmdata = dm.DataSearch(isArea, li, manager_name)
    #Freqdata = FreqTop(dmdata)
    #Freqdata = FreqBottom(dmdata)
    #Freqdata=FreqTop(dmdata)#pd.concat([FreqTop(dmdata),FreqBottom(dmdata)])
    Freqdata = pd.concat([FreqTop(dmdata),FreqBottom(dmdata)], ignore_index=True)
    return Freqdata
    
def FreqTop(dmdata): #Freq=빈도, Top=빈도수 상위
    data=dmdata.value_counts().rename_axis('법정동명').reset_index(name='counts')
    freqtop3=data.head(3)
    #freqper=(freqtop3/len(dmdata))*100
    freqtotal=freqtop3
    return freqtotal

def FreqBottom(dmdata): #Freq=빈도, Bottom=빈도수 하위
    data=dmdata.value_counts(ascending=True).rename_axis('법정동명').reset_index(name='counts')
    freqbottom3=data.head(3)
    #freqper=(freqbottom3/len(dmdata))*100
    freqtotal=freqbottom3
    return freqtotal

print (Recommend(1,1))
#새로 추가된 기능 : 백분율 (top, bottom 데이터 개수만으론 부족한 정보, 해당 개수가 어느정도 비율인지가 더 좋은 정보 제공)
#추가 예정인 기능 : 1. 고유한 데이터의 개수, 2. 전체 데이터의 개수 (코드 이미 작성하였으나, 데이터프레임에 추가하는 도중 사소한 문제 발생)

#def stats(dmdata): #stats = 통계(statistics)
#    data=dmdata.describe()
#    statsdata=pd.DataFrame(data.iloc[:2,-1])
#    return statsdata
