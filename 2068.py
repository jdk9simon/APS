# 2068. 최대수 구하기
'''
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
'''

def compare(numbs):
    num2 = 0
    for num in numbs:
        if  num > num2:
            num2 = num
    return num2

T=int(input())
for t in range(1,T+1):
    case = list(map(int,input().split()))       # case 변수에 list 값을 너준다. map(적용함수, input 값에 뛰어쓰기 적용) 즉 integer 지속적으로 바꿔주면서 모든 값을 반환한후 리스트로 다 변환시킨다.
    print("#{0} {1}".format(t, compare(case))) # f' string 대신 format string 사용. 여기서 {0} 은 loop 통한 t 값을 #1- #3 까지 프린트 그리고 {1} 은 함수 값을 프린트한다.
