# 2071. 평균값 구하기
'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

def average1(numbs):
    return int(round(sum(numbs) / 10, 0))   # 첫째 자리로 round 해준다.

T=int(input())
for t in range(1,T+1):
    case=list(map(int,input().split()))       # case 변수에 list 값을 너준다. map(적용함수, input 값에 뛰어쓰기 적용) 즉 integer 지속적으로 바꿔주면서 모든 값을 반환한후 리스트로 다 변환시킨다.
    print("#{0} {1}".format(t,average1(case))) # f' string 대신 format string 사용. 여기서 {0} 은 loop 통한 t 값을 #1- #3 까지 프린트 그리고 {1} 은 함수 값을 프린트한다.
