# 2056. 연월일 달력
'''
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
'''
# maximum days for each month
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

T=int(input())
for t in range(1,T+1):
    ret = 0   # 0 을 일시적 값
    case = list(map(int,input()))       # case 변수에 list 값을 너준다. map(적용함수, input 값에 뛰어쓰기 적용) 즉 integer 지속적으로 바꿔주면서 모든 값을 반환한후 리스트로 다 변환시킨다.
    m = int(case[4])*10+int(case[5])  # month
    d =int(case[6])*10+int(case[7]) # days
    if not 0 < m < 12: 
        ret = -1
    if not 0 < d <= month[m]:
        ret = -1
    else:
        ret = f'{case[0]}{case[1]}{case[2]}{case[3]}/{case[4]}{case[5]}/{case[6]}{case[7]}'

    print("#{0} {1}".format(t, ret)) # f' string 대신 format string 사용. 여기서 {0} 은 loop 통한 t 값을 #1- #3 까지 프린트 그리고 {1} 은 함수 값을 프린트한다.
                                    # {0} 값에 f string 처럼 t 값이 들어가고 {1} 값에 ret 값이 들어간다.