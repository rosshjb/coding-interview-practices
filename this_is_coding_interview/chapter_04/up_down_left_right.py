"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p110, 상하좌우]
난이도 하, 풀이 시간 15분, 시간 제한 1초, 메모리 제한 128MB
1 <= N <= 100
1 <= MOVES <= 100
"""

n = int(input())
moves = input().split()

next_position = position = 1, 1

for move in moves:
    # determine next position depending on the move
    if move == 'L':
        next_position = (position[0], position[1]-1)
    elif move == 'R':
        next_position = (position[0], position[1]+1)
    elif move == 'U':
        next_position = (position[0]-1, position[1])
    elif move == 'D':
        next_position = (position[0]+1, position[1])

    # if the move will not go outside of the map, then commit it
    if (1 <= next_position[0] <= n) and (1 <= next_position[1] <= n):
        position = next_position

print(position[0], position[1])

