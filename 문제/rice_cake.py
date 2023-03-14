'''
input
4 6
19 15 10 17

output
15
'''

n,m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)

result = 0
while start <= end :
    sum = 0
    mid = (start + end) // 2
    for rice_cake in rice_cakes :
        if rice_cake > mid :
            sum += rice_cake - mid

    if sum < m :
        end = mid - 1
    else :
        result = mid
        start = mid + 1

print(result)