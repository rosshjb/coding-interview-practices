"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p118, 게임 개발]
난이도 중, 풀이 시간 40분, 시간 제한 1초, 메모리 제한 128MB
3 <= N
M <= 50
"""

n, m = map(int, input().split())
x, y, d = map(int, input().split())

the_map = []
for _ in range(n):
    the_map.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
counter = 0

# Add initial position to visited position set
visited = {(x, y)}

direction_list = list(reversed(range(4)))


def determine_direction_list(direction_list):
    for direction in direction_list:
        if direction_list[0] != direction:
            direction_list.append(direction_list.pop(0))
        else:
            direction_list.insert(0, direction_list.pop())
            break


determine_direction_list(direction_list)
while True:
    determine_direction_list(direction_list)

    go_anywhere = False
    # find position which the character can go, from 4 directions.
    for direction in direction_list:
        d = direction
        next_position = (x + dx[d], y + dy[d])
        if the_map[next_position[0]][next_position[1]] == 0 and next_position not in visited:
            x, y = next_position[0], next_position[1]
            visited.add((x, y))
            go_anywhere = True
            break

    if not go_anywhere:
        next_position = (x - dx[d], y - dy[d])
        if the_map[next_position[0]][next_position[1]] == 1:
            break
        else:
            x, y = next_position[0], next_position[1]

print(len(visited))
