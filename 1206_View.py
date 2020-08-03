# 1206. 1일차 View
'''
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input_data/1206.txt')

def compare(bldgs):
    count = 0  # 조망권이 확보된 세대의 숫자
    for bldg in range(2, len(bldgs) - 2):
        # 중간 건물의 높이
        center_height = bldgs[bldg]
        # 2개의 왼쪽 건물들중 더 높은 건물의 높이
        left_height = max(bldgs[bldg-2 : bldg])
        # 왼쪽에 조망권 확보가 가능한지 중간건물의 높이와 비교한다.
        if center_height < left_height:
            continue   # 중간 건물이 낮으면 loop 되돌아가기

        # 2개의 오른쪽 건물들중 더 높은 건물의 높이
        right_height = max(bldgs[bldg+1 : bldg+3])
        # 오른쪽에 조망권 확보가 가능한지 중간건물의 높이와 비교한다.
        if center_height < right_height:
            continue   # 중간 건물이 낮으면 loop 되돌아가기
        # 만약 중간 건물이 조망권 확보가 가능하다면 어느 층 부터 조망권이 확보가 가능한지 확인하기
        # 왼쪽 혹은 오른쪽 둘중에 더 높은 건물의 높이를 찾는다
        obstacle_height = max(left_height, right_height) 
        # 중간 건물의 높이에서 장애물 건물의 높이를 뺀다. 
        count += (center_height - obstacle_height)
    
    return count

# bldgs 변수에 list 값을 너준다. map(적용함수, input 값에 뛰어쓰기 적용) 즉 integer 지속적으로 바꿔주면서 모든 값을 반환한후 리스트로 다 변환시킨다.
# f' string 대신 format string 사용. 여기서 {0} 은 loop 통한 t 값을 #1- #3 까지 프린트 그리고 {1} 은 함수 값을 프린트한다.
# strip() 을 사용하여 가로길이 부분들을 제거해준다.

for t in range(1, 11):
    reduce_to_10_lines = int(input().strip())
    bldgs = list(map(int,input().split()))       
    print("#{0} {1}".format(t, compare(bldgs))) 