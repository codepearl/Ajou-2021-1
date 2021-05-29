import pandas as pd
import datamanager as dm

manager_name="analysismanager"

#def Recommend(isArea, li):
#    dmdata = dm.DataSearch(isArea, li, manager_name)
#    Freqdata = pd.concat([FreqTop(dmdata),FreqBottom(dmdata)], ignore_index=True)
#    return Freqdata
    
def FreqTop(isArea, li): #Freq=빈도, Top=빈도수 상위
    dmdata = dm.DataSearch(isArea, li, manager_name)
    countsdata=dmdata.value_counts().rename_axis('Red Ocean').reset_index(name='Counts')
    perdata=(dmdata.value_counts(normalize=True).rename_axis('Red Ocean').reset_index(name='Percentage'))*100
    perdata.drop('Red Ocean',axis=1,inplace=True)
    perdata=perdata.round(1)
    totaldata=pd.concat([countsdata,perdata],axis=1)
    freqtotal=totaldata.head(15)
    return freqtotal

def FreqBottom(isArea, li): #Freq=빈도, Bottom=빈도수 하위
    dmdata = dm.DataSearch(isArea, li, manager_name)
    countsdata=dmdata.value_counts(ascending=True).rename_axis('Blue Ocean').reset_index(name='Counts')
    perdata=(dmdata.value_counts(normalize=True,ascending=True).rename_axis('Blue Ocean').reset_index(name='Percentage'))*100
    perdata.drop('Blue Ocean',axis=1,inplace=True)
    perdata=perdata.round(1)
    totaldata=pd.concat([countsdata,perdata],axis=1)
    freqtotal=totaldata.head(15)
    return freqtotal

#수정내역
#Blue Ocean, Red Ocean 각각 호출 가능하게 수정.
#각 기능별 상위 15개의 데이터를 반환함.
