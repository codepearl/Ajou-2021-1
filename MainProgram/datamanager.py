import pandas as pd


def DataSearch(isArea, li, manager_name):
    pure_data = pd.read_csv('Dummy_File.csv', encoding='cp949')

    if manager_name == 'mapmanager':
        handled_data = MMSearch(pure_data)
        return handled_data

    elif manager_name == 'graphmanager':
        handled_data = GMSearch(pure_data)
        return handled_data

    elif manager_name == 'analysismanager':
        handled_data = AMSearch(pure_data)
        return handled_data

    elif manager_name == 'scenemanager':
        handled_data = SMSearch(pure_data)
        return handled_data

    else:
        handled_data = SMSearch(pure_data)
        return handled_data


def MMSearch(pure_data):
    mm_data = pd.DataFrame(pure_data, columns=['상호명','경도','위도'])
    return mm_data


def GMSearch(pure_data):
    gm_data = pd.DataFrame(pure_data, columns=['상호명','지점명','상권업종대분류명','상권업종중분류명','상권업종소분류명','시군구명','법정동명'])
    return gm_data

def AMSearch(pure_data):
    am_data = pd.DataFrame(pure_data, columns=['상권업종대분류명','상권업종중분류명','상권업종소분류명','시군구명','법정동명'])
    return am_data

def SMSearch(pure_data):
    sm_data = pd.DataFrame(pure_data)
    return sm_data


if __name__ == '__main__':
    data = DataSearch(1, 2,'mapmanager')
    print(data)

'''
CODE REIVEW by pearl

2. csv에서 Load한 data를 담을 변수 선언 필요(전역 변수)

4. 특정 열만 load하거나, 특정 열만 return 하는 열 처리 과정 필요

5. isArea, li에 따른 data 추리는 과정 필요
'''