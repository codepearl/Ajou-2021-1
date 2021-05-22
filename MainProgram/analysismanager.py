import pandas as pd
import datamanager as dm

manager_name="analysismanager"

def Recommend(isArea, li):
    dmdata = dm.DataSearch(isArea, li, manager_name)
    Freqdata=pd.concat([FreqTop(dmdata),FreqBottom(dmdata)])
    return Freqdata

def FreqTop(dmdata): #Freq=빈도, Top=빈도수 상위
    data=dmdata.value_counts()
    return data.head(3)

def FreqBottom(dmdata): #Freq=빈도, Bottom=빈도수 하위
    data=dmdata.value_counts()
    return data.tail(3)

#dmdata = data from datamanager
