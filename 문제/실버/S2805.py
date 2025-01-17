import sys

n,m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))

def binary_search(tree,start,end) :

    result = 0
    while start <= end :
        mid = (start + end) // 2

        sum = 0
        for i in tree :
            if i <= mid : continue
            sum += (i - mid)

        if sum >= m :
            start = mid + 1
            result = mid
        else : end = mid - 1

    return result

print(binary_search(tree,0,max(tree)))