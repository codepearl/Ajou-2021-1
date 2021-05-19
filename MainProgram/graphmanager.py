import datamanager as dm
import matplotlib.pyplot as plt


def GetGraph(isArea, li, manager_name):
    df = dm.DataSearch(isArea, li, manager_name)
    plt.rc('font', family='NanumGothic')
    return_graph = MakeGraph(df)
    # plt.show()
    return return_graph


def MakeGraph(df):
    xLcategory = df['업종대분류명']
    return_graph = plt.hist(xLcategory)
    return return_graph


# GetGraph(1,2,3)