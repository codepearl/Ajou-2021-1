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


if __name__ == '__main__':
    GetGraph(1, 2, 3)


'''
CODE REIVEW by pearl

1. manager_name 선언 필요.
import 다다음 줄에 선언 부탁합니다.

2. if __name__ == '__main__':
해당줄을 넣으면, graphmanager를 직접적으로 실행했을때에만 해당 부분이 실행됩니다.
다른 곳에서 import를 하거나 실행시켜도 main문은 직접 graphmanager를 실행한게 아니라면
실행되지 않습니다. 그러므로 모듈 테스트는 해당 if 문 안에서 하면 됩니다.

고칠게 더 없어서 아이디어 첨언합니다.
만약 여러 형태의 그래프를 제공할 예정이라면, 그에 대한 함수를 나누고,
sm에 어떤 형태로 만들건지 파라미터를 받아와서 제공을 하는 형태로
해당 모듈의 기능을 더 확장할 수 있을 것 같습니다.
(하라는 얘기는 아니고..^^ 본인의 뛰어남을 증명하기 위해, 더 많은 기능을 넣을 수 있겠죠)

다른 사람들의 경우 띄어쓰기, 줄바꿈, 변수 이름, 함수 이름들을 많이 고쳐줬는데
정말 하나도 고칠 게 없을 정도로 완벽합니다.

저도, GUI에서 고딕폰트를 사용하고 있는데 센스가 엄청나다고 생각합니다.

이 주석은 다음 코딩 때 전부 지우면 됩니다.
'''
