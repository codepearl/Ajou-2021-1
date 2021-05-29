import datamanager as dm
import matplotlib.pyplot as plt
import seaborn as sns

manager_name = "graphmanager"


def GetGraph(isArea, li, manager_name):
    df = dm.DataSearch(isArea, li, manager_name)
    plt.rc('font', family='NanumGothic')
    return_countplot_graph = MakecountplotGraph(df, isArea)
    # return_pie_graph = MakePieGraph(df, isArea)
    # return return_countplot_graph, return_pie_graph
    return return_countplot_graph


def MakecountplotGraph(df, isArea):
    # xLcategory = df['업종대분류명']
    # return_graph = plt.hist(xLcategory)
    if isArea:
        made_countplot_graph = sns.countplot(x='상권업종대분류명', data=df)
    else:
        made_countplot_graph = sns.countplot(x='법정동명', data=df)

    return made_countplot_graph

#
# def MakePieGraph(df, isArea):
#     if isArea:
#         for_pie_df = df['상권업종대분류명']
#         made_pie_graph = for_pie_df.plot.pie(autopct='%.2f%%')
#     else:
#         for_pie_df = df['법정동명']
#         temp = for_pie_df['법정동명'].value_counts()
#         # made_pie_graph = plt.pie(temp, for_pie_df, shadow=True, startangle=90 ) 여기 문제
#     return made_pie_graph


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
