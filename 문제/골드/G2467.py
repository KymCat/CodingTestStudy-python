import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

minMix = 10e9
minLeft = 0
minRight = 0
def solution(start, end) :
    global minMix
    global minLeft
    global minRight

    while start < end :
        mix = arr[start] + arr[end]

        if abs(mix) < minMix :
            minMix = abs(mix)
            minLeft = start
            minRight = end
            if minMix == 0 :
                break
        if mix > 0 :
            end -= 1
        else :
            start += 1

solution(0, n-1)
print(arr[minLeft], arr[minRight])
