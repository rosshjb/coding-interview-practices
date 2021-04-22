"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p178, 위에서 아래로]
난이도 1/3, 풀이 시간 15분, 시간 제한 1초, 메모리 제한 128MB
1 <= N <= 500
"""

n = int(input())

count = [0] * 100001
for _ in range(n):
    count[int(input())] += 1

for i in range(100000, 0, -1):
    for _ in range(count[i]):
        print(i, end=' ')
