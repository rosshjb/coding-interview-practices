"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p96, 숫자 카드 게임]
시간 제한 1초, 메모리 제한 128MB
1 <= N <= 100
1 <= M <= 100
"""

n, m = map(int, input().split())
matrix = []

# Read rows
for _ in range(n):
    # Read each row, and then sort and append it to matrix
    matrix.append(sorted(list(map(int, input().split()))))

# Visit all row to find which row's first element is biggest
biggest = 0
for row in matrix:
    # If the row's first element is bigger, set it to 'biggest'
    if biggest < row[0]:
        biggest = row[0]

# Print biggest number
print(biggest)

