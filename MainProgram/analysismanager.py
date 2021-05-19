import pandas as pd
import datamanager as dm

manager_name = "analysismanager"

def Recommend(isArea, li):
    datas = dm.DataSearch(isArea, li, manager_name)
    Freqdata = pd.concat([FreqTop(datas), FreqBottom(datas)])
    return Freqdata

def FreqTop(datas): #Freq = 빈도, 빈도수 상위
    data = datas.value_counts()
    return data.head(3)

def FreqBottom(datas): #Freq = 빈도, 빈도수 하위
    data = datas.value_counts()
    return data.tail(3)

'''
CODE REIVEW by pearl

FreqT, FreqB -> FreqTop, FreqBottom
testData -> datas


T를 그냥 쓸 경우 True와 혼동될 수 있으므로
Top Bottom 을 끝까지 적는게 좋아보여서 수정하였습니다.

testData 라는 말은 더이상 쓰지 않는게 좋습니다.
test가 아니라 실제로 쓸 Data이기 때문이죠.

datas와 data가 혼동 될 수 있으니 생각해서
더 좋은 이름으로 바꾸면 더욱 더 좋을 것 같습니다.

변수 이름, 띄어쓰기, 줄바꿈만 수정 될 정도로 굉장히 잘 짰습니다.
가장 수정사항이 적습니다. 고생하셨습니다.

이 주석은 다음 코딩 때 전부 지우면 됩니다.
'''
