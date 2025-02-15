import sys
sys.setrecursionlimit(10**9)

arr = []
while True :
    try :
        arr.append(int(sys.stdin.readline()))
    except : break

def post_order(left,right) :
    if left >= right-1 : # 범위가 1개 이하 / right는 현재범위의 노드 개수이므로 -1을 해야함
        print(arr[left])
        return

    if arr[left] > arr[right-1] or arr[left] < arr[left+1] : # 왼쪽 서브트리만 있는 경우 / 오른쪽 서브트리만 있는 경우
        post_order(left+1, right)
        print(arr[left])
        return

    # 왼쪽 오른쪽 서브트리가 섞여 있는 경우
    mid = 0
    for i in range(left+1, right) :
        if arr[left] < arr[i] :
            mid = i
            break

    post_order(left+1,mid)
    post_order(mid,right)
    print(arr[left])

post_order(0,len(arr))