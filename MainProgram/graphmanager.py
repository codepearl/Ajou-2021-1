import datamanager as dm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

manager_name = "graphmanager"


def GetCountplot(isArea, li, manager_name):
    pure_data = dm.DataSearch(isArea, li, manager_name)
    plt.rc('font', family='Malgun Gothic')
    return_countplot = Makecountplot(pure_data, isArea)
    return return_countplot


def GetPie(isArea, li, manager_name):
    pure_data = dm.DataSearch(isArea, li, manager_name)
    plt.rc('font', family='Malgun Gothic')
    return_pie = MakePie(pure_data, isArea)
    return return_pie


def Makecountplot(pure_data, isArea):
    fig = plt.figure(figsize=(10,6))
    fig.set_facecolor('white')
    ax = fig.add_subplot()
    if isArea:
        made_countplot = sns.countplot(x='상권업종대분류명', data=pure_data)
    else:
        made_countplot = sns.countplot(x='법정동명', data=pure_data)
    fig.savefig('graph/count.png')
    return made_countplot


def MakePie(pure_data, isArea):
    # if isArea:
    frequency, labels, explode = MakePieData(pure_data, isArea)

    fig = plt.figure(figsize=(10,6))
    fig.set_facecolor('white')
    ax = fig.add_subplot()

    made_pie = plt.pie(frequency, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, explode=explode)

    #글자 겹침 해결
    total = np.sum(frequency)
    threshold = 5
    sum_pct = 0

    bbox_props = dict(boxstyle='square', fc='w', ec='w', alpha=0)  ## annotation 박스 스타일

    ## annotation 설정
    config = dict(arrowprops=dict(arrowstyle='-'), bbox=bbox_props, va='center')

    for i, l in enumerate(labels):
        ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2  ## 파이의 시작 각도와 끝 각도
        # center, r = ax.patches[i].center, ax.patches[i].r  ## 원의 중심 좌표와 반지름길이

        if i < len(labels) - 1:
            sum_pct += float(f'{frequency[i] / total * 100:.2f}')
            text = f'{frequency[i] / total * 100:.2f}%'
        else:  ## 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
            text = f'{100 - sum_pct:.2f}%'

        ## 비율 상한선보다 작은 것들은 Annotation으로 만든다.
        # if frequency[i] / total * 100 < threshold:
        ang = (ang1 + ang2) / 2  ## 중심각
        x = np.cos(np.deg2rad(ang))  ## Annotation의 끝점에 해당하는 x좌표
        y = np.sin(np.deg2rad(ang))  ## Annotation의 끝점에 해당하는 y좌표

        ## x좌표가 양수이면 즉 y축을 중심으로 오른쪽에 있으면 왼쪽 정렬
        ## x좌표가 음수이면 즉 y축을 중심으로 왼쪽에 있으면 오른쪽 정렬
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)  ## 시작점과 끝점 연결 스타일
        config["arrowprops"].update({"connectionstyle": connectionstyle})  ##
        ax.annotate(text, xy=(x, y), xytext=(1.5 * x, 1.2 * y), horizontalalignment=horizontalalignment, **config)
        # else:
        #     x = (r / 2) * np.cos(np.pi / 180 * ((ang1 + ang2) / 2)) + center[0]  ## 텍스트 x좌표
        #     y = (r / 2) * np.sin(np.pi / 180 * ((ang1 + ang2) / 2)) + center[1]  ## 텍스트 y좌표
        #     ax.text(x, y, text, ha='center', va='center', fontsize=12)
    plt.legend(made_pie[0], labels, loc='upper right')

    fig.savefig('graph/pie.png')
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
        explode = []
        for i in list_filtered_data2:
            count_list.append((list_filtered_data.count(i)))
        for j in count_list:
            ratio_list.append(j / len(list_filtered_data) * 100)
            explode.append(0.1)
    else:
        list_filtered_data = pure_data['법정동명'].tolist()
        set_filtered_data = set(list_filtered_data)
        list_filtered_data2 = list(set_filtered_data)
        count_list = []
        ratio_list = []
        explode = []
        for i in list_filtered_data2:
            count_list.append((list_filtered_data.count(i)))
        for j in count_list:
            ratio_list.append(j / len(list_filtered_data) * 100)
            explode.append(0.1)
    return ratio_list, list_filtered_data2, explode


if __name__ == '__main__':
    #return_graph = GetCountplot(False, ['음식', '한식', '갈비/삼겹살'], "graphmanager")
    return_graph = GetPie(False, ['음식', '한식', '갈비/삼겹살'], "graphmanager")
    plt.show()

'''
CODE REIVEW by pearl

고칠게 더 없어서 아이디어 첨언합니다.
만약 여러 형태의 그래프를 제공할 예정이라면, 그에 대한 함수를 나누고,
sm에 어떤 형태로 만들건지 파라미터를 받아와서 제공을 하는 형태로
해당 모듈의 기능을 더 확장할 수 있을 것 같습니다.
(하라는 얘기는 아니고..^^ 본인의 뛰어남을 증명하기 위해, 더 많은 기능을 넣을 수 있겠죠)
'''
