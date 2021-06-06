import pandas as pd

#pure_data = pd.read_csv('data/Merge_File_All_Col_Remove_r2.csv', encoding='cp949')
pure_data = pd.read_csv('data/Dummy_File.csv', encoding='cp949')


def DataSearch(isArea, li, manager_name):
    if manager_name != 'mapmanager':
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
    else:
        m_district = pure_data['시군구명'] == li[0]
        s_district = pure_data['법정동명'] == li[1]
        l_class = pure_data['상권업종대분류명'] == li[2]
        m_class = pure_data['상권업종중분류명'] == li[3]
        s_class = pure_data['상권업종소분류명'] == li[4]
        input_based_data = pure_data[m_district & s_district & l_class & m_class & s_class]

    if manager_name == 'mapmanager':
        handled_data = MMSearch(input_based_data)

    elif manager_name == 'graphmanager':
        handled_data = GMSearch(input_based_data)

    elif manager_name == 'analysismanager':
        handled_data = AMSearch(input_based_data, isArea)

    elif manager_name == 'scenemanager':
        handled_data = SMSearch(input_based_data)

    else:
        handled_data = SMSearch(input_based_data)

    return handled_data


def MMSearch(input_based_data):
    mm_data = pd.DataFrame(input_based_data, columns=['상권업종대분류명', '상호명','경도','위도'])
    return mm_data


def GMSearch(input_based_data):
    gm_data = pd.DataFrame(input_based_data, columns=['상권업종대분류명','상권업종중분류명','상권업종소분류명','시군구명','법정동명'])
    return gm_data


def AMSearch(input_based_data, isArea):
    if isArea:
        am_data = pd.DataFrame(input_based_data, columns=['상권업종소분류명'])
    else:
        am_data = pd.DataFrame(input_based_data, columns=['법정동명'])
    return am_data


def SMSearch(input_based_data):
    sm_data = pd.DataFrame(input_based_data)
    return sm_data


# SM에 입력 list data 제공
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

'''
CODE REIVEW by pearl
2. csv에서 Load한 data를 담을 변수 선언 필요(전역 변수)
'''
