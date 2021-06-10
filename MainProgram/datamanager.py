########################################################################
#                                                                      #
#   @copyright  Copyright (c) 2021 Pear129, All rights reserved.       #
#   @author     prawnboat-249                                          #
#   @Ajou       융합시스템공학과 이새결  202020638                         #
#                                                                      #
########################################################################

# Import modules
import pandas as pd


pure_data = pd.read_csv('data/Dummy_File.csv', encoding='cp949')                    # csv 파일 불러오기


def DataSearch(isArea, li, manager_name):                   # 다른 모듈에서 필요한 데이터를 생성 및 반환
    if manager_name != 'mapmanager':                    # 이 함수를 사용하는 모듈이 mapmanager가 아닌 나머지 모듈이라면,
        if isArea:                  # 입력 데이터가 지역 데이터라면,
            m_district = pure_data['시군구명'] == li[0]
            s_district = pure_data['법정동명'] == li[1]
            input_based_data = pure_data[m_district & s_district]
        else:                  # 입력 데이터가 업종 데이터라면,
            l_class = pure_data['상권업종대분류명'] == li[0]
            m_class = pure_data['상권업종중분류명'] == li[1]
            s_class = pure_data['상권업종소분류명'] == li[2]
            input_based_data = pure_data[l_class & m_class & s_class]
    else:                    # 이 함수를 사용하는 모듈이 mapmanager라면,
        m_district = pure_data['시군구명'] == li[0]
        s_district = pure_data['법정동명'] == li[1]
        l_class = pure_data['상권업종대분류명'] == li[2]
        m_class = pure_data['상권업종중분류명'] == li[3]
        s_class = pure_data['상권업종소분류명'] == li[4]
        input_based_data = pure_data[m_district & s_district & l_class & m_class & s_class]

    if manager_name == 'mapmanager':                    # 이 함수를 사용하는 모듈이 mapmanager라면,
        handled_data = MMSearch(input_based_data)                   # MMsearch를 사용하여 생성한 data를 저장

    elif manager_name == 'graphmanager':                    # 이 함수를 사용하는 모듈이 graphmanager라면,
        handled_data = GMSearch(input_based_data)                   # GMsearch를 사용하여 생성한 data를 저장

    elif manager_name == 'analysismanager':                    # 이 함수를 사용하는 모듈이 analysismanager라면,
        handled_data = AMSearch(input_based_data, isArea)                   # AMsearch를 사용하여 생성한 data를 저장

    elif manager_name == 'scenemanager':                    # 이 함수를 사용하는 모듈이 scenemanager라면,
        handled_data = SMSearch(input_based_data)                   # SMsearch를 사용하여 생성한 data를 저장

    else:                   # 프르그램 오류 방지를 위한 예외 설정
        handled_data = SMSearch(input_based_data)

    return handled_data


# MapManager에 필요한 데이터를 생성하는 함수
def MMSearch(input_based_data):
    mm_data = pd.DataFrame(input_based_data, columns=['상권업종대분류명', '상호명','경도','위도'])
    return mm_data


# GraphManager에 필요한 데이터를 생성하는 함수
def GMSearch(input_based_data):
    gm_data = pd.DataFrame(input_based_data, columns=['상권업종대분류명','상권업종중분류명','상권업종소분류명','시군구명','법정동명'])
    return gm_data

# AnalysisManager에 필요한 데이터를 생성하는 함수
def AMSearch(input_based_data, isArea):
    if isArea:
        am_data = pd.DataFrame(input_based_data, columns=['상권업종소분류명'])
    else:
        am_data = pd.DataFrame(input_based_data, columns=['법정동명'])
    return am_data


# SceneManager에 필요한 데이터를 생성하는 함수
def SMSearch(input_based_data):
    sm_data = pd.DataFrame(input_based_data)
    return sm_data


# 사용자의 입력을 받기 위한 combo box에 제공될 데이터를 SceceManager에 제공
    # 지역
def ListMDistrict():
    return pure_data['시군구명'].unique()


def ListSDistrict(m_district):
    filtered_data = pure_data[pure_data['시군구명'] == m_district]
    return filtered_data['법정동명'].unique()

    # 업종분류
def ListLCategory():
    return pure_data['상권업종대분류명'].unique()


def ListMCategory(l_district):
    filtered_data = pure_data[pure_data['상권업종대분류명'] == l_district]
    return filtered_data['상권업종중분류명'].unique()


def ListSCategory(m_district):
    filtered_data = pure_data[pure_data['상권업종중분류명'] == m_district]
    return filtered_data['상권업종소분류명'].unique()


if __name__ == '__main__':
    temp_list = ['세종특별자치시', '조치원읍', '음식', '유흥주점', '호프/맥주']
    data = DataSearch(True, temp_list,'mapmanager')
    # data = ListSDistrict('세종특별자치시')
    # data = ListMDistrict()
    # data = ListSCategory('개인서비스')
    print(data)