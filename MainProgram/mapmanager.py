import folium
from folium.plugins import MarkerCluster
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
    mapData = ShowLoc()
    return mapData
    
    
def GetLoc (): #(request_type, li): #Datamanager return
    return dm.DataSearch(True, "Test", manager_name) #(request_type, li, manager_name) # 해당 조건에 부합하는 Data Frame return 받음 ex) 위도,경도, 상호명, etc..(지도에 표시할 내용)


def ShowLoc (): #(request_type, li): # 위도,경도, 상호명, etc..(지도에 표시할 내용) 받아서 맵에서 표시
    data = GetLoc() #(request_type, li)
    lat = data['위도'].mean()
    lng = data['경도'].mean()
    list1=[]
    list2=[]
    map = folium.Map(tiles='Stamen Terrain', location = [lat,lng], zoom_start=11)
    marker_cluster = MarkerCluster().add_to(map)
    for a in range(1,1000): #data.index: // 현재 데이터 3000개가 넘어가면 지도가 안열려서 우선 range 넣음 / 진주컴 1000개 기준
        folium.Marker(location = [data.loc[a,"위도"],data.loc[a,"경도"]],zoom_start=11,
                      popup=data.loc[a,"상호명"]).add_to(marker_cluster)
        list1.append(data.loc[a,"위도"])
        list2.append(data.loc[a,"경도"])
    
    #map.save('map_test.html')
    
    return map

#print (ShowLoc())

'''

1. request_type 에 대한 변수 선언 필요
manager_name 다다음 라인에 임시 int 넣어서 변수 선언하세요.


sm에서 Map을 호출해 request_type과 string list들을 넘겨줄 예정입니다.

ShowLoc을 호출하여 결과값을 mapData에 담아 sm에 돌려줄 것입니다.


'''
