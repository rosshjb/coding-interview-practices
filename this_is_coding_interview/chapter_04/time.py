"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p113, 시각]
난이도 하, 풀이 시간 15분, 시간 제한 2초, 메모리 제한 128MB
0 <= N <= 23
"""

n = int(input())

time_string = '000000'
counter = 0

for _ in range(86400):
    # count if the string contains number 3.
    if '3' in time_string:
        counter += 1

    # increment time
    time_string = time_string[:4] + '{:0=2d}'.format(int(time_string[4:]) + 1)

    # calculate minutes
    if int(time_string[4:]) > 59:
        time_string = time_string[0:2] + '{:0=2d}'.format(int(time_string[2:4]) + 1) + '00'

    # calculate hours
    if int(time_string[2:4]) > 59:
        time_string = '{:0=2d}'.format(int(time_string[0:2]) + 1) + '00' + time_string[4:]

    # break loop if the time is over the provided end-time.
    if int(time_string) > int('{:0=2d}5959'.format(n)):
        break

print(counter)

