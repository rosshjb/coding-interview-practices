"""
이것이 취업을 위한 코딩 테스트다 - 나동빈[p178, 성적이 낮은 순서로 학생 출력하기]
난이도 1/3, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB
1 <= N <= 100,000
"""

n = int(input())

students = []
for _ in range(n):
    name, grade = input().split()
    students.append((name, int(grade)))

count = [[] for _ in range(101)]
for i in range(n):
    name = students[i][0]
    grade = students[i][1]
    count[grade].append(name)

for students in count:
    for student in students:
        print(student, end=' ')
