import pandas as pd


def DataSearch(isArea, li, manager_name):
    temp_data = {'상호': ['숙성1퍼센트', '죠스떡볶이'], '지점명': ['NaN', '탑동점'],
                 '업종대분류명': ['음식', '음식'], '업종중분류명':['한식', '분식'], '업종소분류명': ['한식/백반/한정식', '떡볶이전문'],
                 '시군구명': ['제주시', '제주시'], '법정동명': ['노형동', '건입동'], '경도': [126.4798935, 126.5267972], '위도': [33.48333476, 33.51673654]}

    data = pd.DataFrame(temp_data)
    return data


# data = DataSearch(1, 2, 3)
# print(data)
