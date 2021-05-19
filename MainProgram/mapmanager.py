import folium
import pandas as pd
import datamanager as dm
import scenemanager as sm

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

def Requestdata(): # scenemanager Requestdata

    request_type, data = sm.request()

    return reqest_type, data
    
    
def Getloc(): # Datamanager return

    request_type, li = requestdata()
    
    return dm.DataSearch( request_type , li , manager_name) # 해당 조건에 부합하는 Data Frame return 받음 ex) 위도,경도, 상호명, etc..(지도에 표시할 내용)


def Showloc(): # 위도,경도, 상호명, etc..(지도에 표시할 내용) 받아서 맵에서 표시

    data = Getloc()

    



