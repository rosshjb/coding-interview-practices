"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p115, 왕실의 나이트]
난이도 하, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB
"""

# Read column and row
column, row = list(input())

row = int(row)
column = ord(column) - 96

counter = 0
# Check all directions to whether it can move
# Up-right
if row - 2 >= 1 and column + 1 <= 8:
    counter += 1
# Up-left
if row - 2 >= 1 and column - 1 >= 1:
    counter += 1
# Down-right
if row + 2 <= 8 and column + 1 <= 8:
    counter += 1
# Down-left
if row + 2 <= 8 and column - 1 >= 1:
    counter += 1
# Right-up
if row - 1 >= 1 and column + 2 <= 8:
    counter += 1
# Right-down
if row + 1 <= 8 and column + 2 <= 8:
    counter += 1
# Left-up
if row - 1 >= 1 and column - 2 >= 1:
    counter += 1
# Left-down
if row + 1 <= 8 and column - 2 >= 1:
    counter += 1

print(counter)
