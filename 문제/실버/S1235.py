import sys

n = int(input())

students = []
for _ in range(n) :
    num = sys.stdin.readline().rstrip()[::-1]
    students.append(num)

for i in range(1,len(students[0])+1) :
    ans = set()
    for student in students :
        ans.add(student[:i])

    if len(ans) == len(students) :
        print(i)
        break




