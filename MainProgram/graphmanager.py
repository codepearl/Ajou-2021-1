import datamanager as dm
import matplotlib.pyplot as plt
import seaborn as sns

manager_name = "graphmanager"


def GetGraph(isArea, li, manager_name):
    pure_data = dm.DataSearch(isArea, li, manager_name)
    plt.rc('font', family='NanumGothic')
    return_countplot = MakecountplotGraph(pure_data, isArea)
    return_pie = MakePieGraph(pure_data, isArea)
    return return_countplot, return_pie
    # return return_countplot_graph


def MakecountplotGraph(pure_data, isArea):
    if isArea:
        made_countplot = sns.countplot(x='상권업종대분류명', data=pure_data)
    else:
        made_countplot = sns.countplot(x='법정동명', data=pure_data)

    return made_countplot


def MakePieGraph(pure_data, isArea):
    # if isArea:
    ratio_list, labels_list = MakePieData(pure_data, isArea)
    made_pie = plt.pie(ratio_list, labels=labels_list, autopct='%.1f%%')
    # else:
    #     ratio_list, labels_list = MakePieData(pure_data, isArea)
    #     made_pie = plt.pie(ratio_list, labels=labels_list, autopct='%.1f%%')
    return made_pie


def MakePieData(pure_data, isArea):
    if isArea:
        list_filtered_data = pure_data['상권업종소분류명'].tolist()
        set_filtered_data = set(list_filtered_data)
        list_filtered_data2 = list(set_filtered_data)
        count_list = []
        ratio_list = []
        for i in list_filtered_data2:
            count_list.append((list_filtered_data.count(i)))
        for j in count_list:
            ratio_list.append(j / len(list_filtered_data) * 100)
    else:
        list_filtered_data = pure_data['법정동명'].tolist()
        set_filtered_data = set(list_filtered_data)
        list_filtered_data2 = list(set_filtered_data)
        count_list = []
        ratio_list = []
        for i in list_filtered_data2:
            count_list.append((list_filtered_data.count(i)))
        for j in count_list:
            ratio_list.append(j / len(list_filtered_data) * 100)
    return ratio_list, list_filtered_data2


if __name__ == '__main__':
    test_return_graph1 = GetGraph(True, ['세종특별자치시', '조치원읍'], "graphmanager")
    # test_return_graph1 = GetGraph(False, ['음식', '한식', '갈비/삼겹살'], "graphmanager")
    plt.show()

'''
CODE REIVEW by pearl

고칠게 더 없어서 아이디어 첨언합니다.
만약 여러 형태의 그래프를 제공할 예정이라면, 그에 대한 함수를 나누고,
sm에 어떤 형태로 만들건지 파라미터를 받아와서 제공을 하는 형태로
해당 모듈의 기능을 더 확장할 수 있을 것 같습니다.
(하라는 얘기는 아니고..^^ 본인의 뛰어남을 증명하기 위해, 더 많은 기능을 넣을 수 있겠죠)
'''
