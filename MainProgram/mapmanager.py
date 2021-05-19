import folium
import pandas as pd
import datamanager as dm

manager_name = "mapmanager"

'''
    if isArea == 0:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)

    elif isArea == 1:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)

    elif isArea == 2:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)

    elif isArea == 3:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)

    elif isArea == 4:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)
        
    elif isArea == 5:
        print('```') # 위도,경도, 상호명, etc..(지도에 표시할 내용)
'''

# 시군구, 업종 대분류 받고 넘겨줌 – 0 
# 시군구, 업종 대분류/중분류 넘겨줌 – 1                    
# 시군구, 업종 대분류/중분류/소분류 넘겨줌 – 2 
# 시군구/법정동, 업종 대분류 넘겨줌 - 3
# 시군구/법정동, 업종 대분류/중분류 넘겨줌 - 4
# 시군구/법정동, 업종 대분류/중분류/소분류 넘겨줌 -5

# 위에 0,1,2,3,4,5는 request_type

def Map(request_type, li): #call from scenemanager
    mapData = ShowLoc(request_type, li)
    return mapData
    
    
def GetLoc(request_type, li): # Datamanager return
    return dm.DataSearch(request_type, li, manager_name) # 해당 조건에 부합하는 Data Frame return 받음 ex) 위도,경도, 상호명, etc..(지도에 표시할 내용)


def ShowLoc(request_type, li): # 위도,경도, 상호명, etc..(지도에 표시할 내용) 받아서 맵에서 표시
    data = Getloc(request_type, li)
    #folium 사용해서 지도에 표시
    return data
    
'''
CODE REIVEW by pearl

Getloc, Showloc -> GetLoc, ShowLoc

1. request_type 에 대한 변수 선언 필요
manager_name 다다음 라인에 임시 int 넣어서 변수 선언하세요.

2. 아직 각 모듈 간 과정에 대한 이해가 조금 부족한 것 같습니다.
sm에서 mm의 함수를 호출하는 형식이므로, mm에서는 sm을 호출할 필요는 없습니다.
->import scenemanager 삭제
그러므로 Requestdata 아닌, sm에서 호출될 이름으로 변경하는게 좋습니다.
Requestdata() -> Map(request_type, li)

sm에서 Map을 호출해 request_type과 string list들을 넘겨줄 예정입니다.

ShowLoc을 호출하여 결과값을 mapData에 담아 sm에 돌려줄 것입니다.

일단 최대한 구조를 냅두면서 각 함수를 조금 수정해봤습니다.

GetLoc/ShowLoc에 각각 파라미터를 추가함으로써,
sm에서 호출될 때 받아온 값들을 dm에 넘겨 데이터들을 받고 -> GetLoc의 내용
folium 사용해서 지도에 표시합니다. ->ShowLoc의 내용

각 함수 정의가 매우 마음에 듭니다.
mapmanager 이 모듈 하나에 대한 이해는 매우 좋아 기대가 됩니다.

이 주석은 다음 코딩 때 전부 지우면 됩니다.
'''
