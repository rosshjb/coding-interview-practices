"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p92, 큰 수의 법칙]
시간 제한 1초, 메모리 제한 128MB
2 <= N <= 1,000
1 <= M <= 10,000
1 <= K <= 10,000
"""

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

decreasing_array = sorted(array, reverse=True)  # [6, 5, 4, 4, 2]
addend = 0
adder = decreasing_array[0]
count = k

for _ in range(m):
    # If count is smaller than k, we set adder to biggest number.
    if count < k:
        adder = decreasing_array[0]

    # Add adder to addend, and then decrease count.
    addend += adder
    count -= 1

    # If count was exhausted, we set the adder to second biggest number.
    # The count should be recovered.
    if count <= 0:
        adder = decreasing_array[1]
        count = k

# print the sum
print(addend)

