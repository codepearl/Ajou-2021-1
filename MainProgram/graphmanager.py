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
    fig = plt.figure(figsize=(10, 6))
    fig.set_facecolor('white')
    ax = fig.add_subplot()
    if isArea:
        made_countplot = sns.countplot(x='상권업종대분류명', data=pure_data, )
    else:
        made_countplot = sns.countplot(x='법정동명', data=pure_data)

    plt.xticks(rotation=45)
    fig.savefig('graph/count.png', bbox_inches='tight')#, pad_inches=0)
    return made_countplot


def MakePie(pure_data, isArea):
    frequency, labels = MakePieData(pure_data, isArea)  # MakePieData 함수를 통해 Pie 그래프를 위한 데이터를 반환 받음

    fig = plt.figure(figsize=(10, 6))  # 캔버스 생성
    fig.set_facecolor('white')  # 배경색 설정
    ax = fig.add_subplot()  # 프레임 생성

    made_pie = plt.pie(frequency,  # Pie graph 생성 (
                       # autopct='%.1f%%',                    # 글자 겹침으로 사용하지 않음
                       startangle=90,  # 시작점을 90도로 설정
                       counterclock=False)  # 시계방향으로 그려짐
    # 글자 겹침 해결 시작
    total = np.sum(frequency)  # 빈도수 합
    threshold = 5  # 상한선 비율
    sum_pct = 0  # 퍼센티지

    bbox_props = dict(boxstyle='square', fc='w', ec='w', alpha=0)  # annotation 박스 스타일

    # annotation 설정
    config = dict(arrowprops=dict(arrowstyle='-'), bbox=bbox_props, va='center')

    for i, l in enumerate(labels):
        ang1, ang2 = ax.patches[i].theta1, ax.patches[i].theta2  # 파이의 시작 각도와 끝 각도
        center, r = ax.patches[i].center, ax.patches[i].r  # 원의 중심 좌표와 반지름길이

        if i < len(labels) - 1:
            sum_pct += float(f'{frequency[i] / total * 100:.2f}')
            text = f'{frequency[i] / total * 100:.2f}%'
        else:  # 마지막 파이 조각은 퍼센티지의 합이 100이 되도록 비율을 조절
            text = f'{100 - sum_pct:.2f}%'

        # 비율 상한선보다 작은 것들은 annotation으로 표시.
        if frequency[i] / total * 100 < threshold:
            ang = (ang1 + ang2) / 2  # 중심각
            x = np.cos(np.deg2rad(ang))  # Annotation의 끝점에 해당하는 x좌표
            y = np.sin(np.deg2rad(ang))  # Annotation의 끝점에 해당하는 y좌표

            # x좌표가 양수이면, 즉 y축을 중심으로 오른쪽에 있으면 왼쪽 정렬
            # x좌표가 음수이면, 즉 y축을 중심으로 왼쪽에 있으면 오른쪽 정렬
            horizontal_alignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connection_style = "angle,angleA=0,angleB={}".format(ang)  ## 시작점과 끝점 연결 스타일
            config["arrowprops"].update({"connectionstyle": connection_style})
            added_text = text + '\n' + l
            ax.annotate(added_text, xy=(x, y), xytext=(1.5 * x, 1.2 * y), horizontalalignment=horizontal_alignment,
                        **config)
        else:
            x = (r / 2) * np.cos(np.pi / 180 * ((ang1 + ang2) / 2)) + center[0]                 # 텍스트 x좌표
            y = (r / 2) * np.sin(np.pi / 180 * ((ang1 + ang2) / 2)) + center[1]                 # 텍스트 y좌표
            added_text = text + '\n' + l
            ax.text(x, y, added_text, ha='center', va='center', fontsize=12)
    # plt.legend(made_pie[0], labels, loc='right')                  # 필요성이 적어서 범례 사용하지 않음

    fig.savefig('graph/pie.png')#, bbox_inches='tight')#, pad_inches=0)

    return made_pie


def MakePieData(pure_data, isArea):                 # Pie graph 를 만들기 위한 data 를 생성하는 함수
    if isArea:                  # 입력데이터가 지역과 업종 중 지역이라면,
        list_filtered_data = pure_data['상권업종소분류명'].tolist()                 # 업종소분류 데이터를 리스트로 저장
        set_filtered_data = set(list_filtered_data)                 # 중복 데이터 제거를 위해 set으로 변환
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

    etc_sum = 0                 # 백분율이 기준보다 낮으면 데이터를 기타로 묶음
    del_list = []
    for i, k in enumerate(ratio_list):                 # ratio_list 와 list_filtered_data2에서 기준 미만에 해당하는 요소를 지우기 위한 index
        if k < 2:                   # 기준을 2%로 설정
            etc_sum += k                # 기타의 합 누적
            del_list.append(i)                  # 요소 삭제를 위한 index list

    while len(del_list) != 0:                   # pop 을 사용할 예정으로, del_list 의 요소가 없으면 종료
        del_index = del_list.pop()
        del ratio_list[del_index]                   # del_index 를 사용하여 기준 미만의 ratio_list 요소 제거
        del list_filtered_data2[del_index]                  # del_index 를 사용하여 기준 미만의 list_filtered_data2 요소 제거

    ratio_list.append(etc_sum)                  # ratio_list 에 '기타' 항목에 해당하는 값 추가
    list_filtered_data2.append("기타")                    # ratio_list 에 '기타' 항목 추가

    return ratio_list, list_filtered_data2


if __name__ == '__main__':
    # return_graph = GetCountplot(False, ['음식', '한식', '갈비/삼겹살'], "graphmanager")
    # return_graph = GetPie(True, ['세종특별자치시', '나성동'], "graphmanager")
    return_graph = GetPie(False, ['음식', '한식', '갈비/삼겹살'], "graphmanager")
    plt.show()
