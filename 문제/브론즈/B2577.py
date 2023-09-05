result = [0] * 10

mul = 1
for _ in range(3) :
    mul *= int(input())

for i in str(mul) :
    result[int(i)] += 1

for i in result :
    print(i)