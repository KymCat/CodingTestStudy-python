'''
input
4
jung 51
dong 160
back 120
pang 89

output
dong
back
pang
'''

# IQ가 높은 순서대로 상위 3명의 이름을 3줄에 걸쳐 출력

n = int(input())
students = []
for _ in range(n) :
    name, iq = input().split()
    students.append((name, int(iq)))

students = sorted(students, reverse = True, key = lambda x:x[1])
for names in students[:3] :
    print(names[0])