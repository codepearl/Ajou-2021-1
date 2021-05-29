import pandas as pd


def DataSearch(isArea, li, manager_name):
    pure_data = pd.read_csv('Dummy_File.csv', encoding='cp949')

    if isArea:
        # 입력으로 지역이 될 경우, 현재 2개 모두 입력되어야 함
        m_district = pure_data['시군구명'] == li[0]
        s_district = pure_data['법정동명'] == li[1]
        input_based_data = pure_data[m_district & s_district]
    else:
        # 입력으로 업종이 입력될 경우, 현재 3개 모두 입력되어야 함
        l_class = pure_data['상권업종대분류명'] == li[0]
        m_class = pure_data['상권업종중분류명'] == li[1]
        s_class = pure_data['상권업종소분류명'] == li[2]
        input_based_data = pure_data[l_class & m_class & s_class]

    if manager_name == 'mapmanager':
        handled_data = MMSearch(input_based_data)

    elif manager_name == 'graphmanager':
        handled_data = GMSearch(input_based_data)

    elif manager_name == 'analysismanager':
        handled_data = AMSearch(input_based_data)

    elif manager_name == 'scenemanager':
        handled_data = SMSearch(input_based_data)

    else:
        handled_data = SMSearch(input_based_data)

    return handled_data


def MMSearch(pure_data):
    mm_data = pd.DataFrame(pure_data, columns=['상호명','경도','위도'])
    return mm_data


def GMSearch(pure_data):
    gm_data = pd.DataFrame(pure_data, columns=['상호명','지점명','상권업종대분류명','상권업종중분류명','상권업종소분류명','시군구명','법정동명'])
    return gm_data

def AMSearch(pure_data):
    am_data = pd.DataFrame(pure_data["법정동명"])
    return am_data

def SMSearch(pure_data):
    sm_data = pd.DataFrame(pure_data)
    return sm_data


if __name__ == '__main__':
    temp_list = ['세종특별자치시', '부강면']
    data = DataSearch(True, temp_list,'datamanager')
    print(data)

'''
CODE REIVEW by pearl
2. csv에서 Load한 data를 담을 변수 선언 필요(전역 변수)
'''
