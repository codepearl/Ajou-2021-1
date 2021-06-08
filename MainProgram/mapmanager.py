import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
import datamanager as dm

manager_name = "mapmanager"


def Map(request_type, li): #call from scenemanager
    mapData = ShowLoc( li )
    return mapData
    
    
def GetLoc ( li ): #Datamanager return
    return dm.DataSearch(True, li, manager_name) # 해당 조건에 부합하는 Data Frame return 받음 ex) 위도,경도, 상호명, etc..(지도에 표시할 내용)


def StartMap (): #Start Map Location
    coordinate = (36.3, 127.8) # Map Show Mid Point
    m = folium.Map(
        tiles='cartodbpositron',
        zoom_start=7,
        location=coordinate
        )
    return m

def ShowLoc ( li ): # 위도,경도, 상호명, etc..(지도에 표시할 내용) 받아서 맵에서 표시
    data = GetLoc( li )
    lat = data['위도'].mean()
    lng = data['경도'].mean()
    np_lat = np.array(lat)
    np_lng = np.array(lng)
    
    map = folium.Map(tiles='cartodbpositron',
                     location = [lat,lng],
                     zoom_start=10) 
    
    marker_cluster = MarkerCluster().add_to(map)
     
    for a in data.index:
        if data.loc[a,'상권업종대분류명'] == '음식':
            color = 'red'
            icon = 'cutlery'
        elif data.loc[a,'상권업종대분류명'] == '관광/여가/오락':
            color = 'blue'
            icon = 'plane'
        elif data.loc[a,'상권업종대분류명'] == '생활서비스':
            color = 'darkpurple'
            icon = 'info-sign'
        elif data.loc[a,'상권업종대분류명'] == '소매':
            color = 'pink'
            icon = 'shopping-cart'
        elif data.loc[a,'상권업종대분류명'] == '숙박':
            color = 'orange'
            icon = 'home'
        elif data.loc[a,'상권업종대분류명'] == '스포츠':
            color = 'green'
            icon = 'heart'
        elif data.loc[a,'상권업종대분류명'] == '학문/교육':
            color = 'gray'
            icon = 'pencil'
        elif data.loc[a,'상권업종대분류명'] == '부동산':
            color = 'beige'
            icon = 'flag'
            
        folium.Marker(location = [data.loc[a,"위도"],data.loc[a,"경도"]],
                      zoom_start=11,
                      popup = ["위도:",data.loc[a,"위도"],"경도:",data.loc[a,"경도"]],
                      tooltip = data.loc[a,"상호명"],
                      icon=folium.Icon( color = color, icon = icon )).add_to(marker_cluster)
        
    
    return map
