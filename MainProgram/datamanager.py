import pandas as pd


def DataSearch(isArea, li, manager_name):
    data = pd.read_csv('Dummy_File.csv', encoding='cp949')
    return data


if __name__ == '__main__':
    data = DataSearch(1, 2, 3)
    print(data)

'''
CODE REIVEW by pearl

1. csvLoad 필요

2. csv에서 Load한 data를 담을 변수 선언 필요(전역 변수)

3. manager_name에 따라 다르게 처리하는 과정 필요

4. 특정 열만 load하거나, 특정 열만 return 하는 열 처리 과정 필요

5. isArea, li에 따른 data 추리는 과정 필요

6. if __name__ == '__main__':
해당줄을 넣으면, graphmanager를 직접적으로 실행했을때에만 해당 부분이 실행됩니다.
다른 곳에서 import를 하거나 실행시켜도 main문은 직접 datamanager를 실행한게 아니라면
실행되지 않습니다. 그러므로 모듈 테스트는 해당 if 문 안에서 하면 됩니다.

우리 프로그램의 꽃 datamanager입니다. 매우 분량이 많아 걱정이 되는데
분명 잘 해낼거라고 믿습니다 ㅎㅎ 잘 해낸 만큼 점수도 잘 받아갈수 있는거니까요~

다른 사람들의 경우 띄어쓰기, 줄바꿈, 변수 이름, 함수 이름들을 많이 고쳐줬는데
정말 하나도 고칠 게 없을 정도로 완벽합니다.

이 주석은 다음 코딩 때 전부 지우면 됩니다.
'''
