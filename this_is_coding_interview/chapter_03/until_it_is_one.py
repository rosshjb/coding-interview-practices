"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p99, 1이 될 때까지]
시간 제한 1초, 메모리 제한 128MB
2 <= N <= 100,000
2 <= K <= 100,000
K <= N
"""

n, k = map(int, input().split())

counter = 0

while n > 1:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    counter += 1

print(counter)
