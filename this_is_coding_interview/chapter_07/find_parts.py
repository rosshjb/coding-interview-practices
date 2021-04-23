"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p197, 부품 찾기]
난이도 1.5/3, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB
1 <= N <= 1,000,000
1 <= M <= 100,000
"""

n = int(input())
shop_parts = list(map(int, input().split()))

m = int(input())
cust_parts = list(map(int, input().split()))

for part in cust_parts:
    if part in shop_parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')


############## 이진 탐색을 이용한 풀이
# sorted_shop_parts = sorted(shop_parts)
# start = 0
# end = n - 1
#
# for part in cust_parts:
#     while start <= end:
#         middle = (start + end) // 2
#
#         if sorted_shop_parts[middle] == part:
#             print('yes', end=' ')
#             start, end = 0, n - 1
#             break
#         else:
#             if start >= end:
#                 print('no', end=' ')
#                 start, end = 0, n - 1
#                 break
#
#             if sorted_shop_parts[middle] > part:
#                 end = middle - 1
#             elif sorted_shop_parts[middle] < part:
#                 start = middle + 1
