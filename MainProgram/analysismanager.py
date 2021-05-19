import pandas as pd
import datamanager as dm

manager_name="test"

def Recommend(isArea, li):
    testData = dm.DataSearch(isArea, li, manager_name)
    Freqdata=pd.concat([FreqT(testData),FreqB(testData)])
    return Freqdata
    
def FreqT(testData): #Freq=빈도, T=Top, 빈도수 상위
    data=testData.value_counts()
    return data.head(3)


def FreqB(testData): #Freq=빈도, B=Bottom, 빈도수 하위
    data=testData.value_counts()
    return data.tail(3)
