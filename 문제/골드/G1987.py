import sys

r,c = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(r)]
for i in range(r) :
    graph[i] = list(sys.stdin.readline().rstrip())

visited = [[0]*c for _ in range(r)]
def dfs(start, end, visited, bit, cnt) :
    max_cnt = cnt

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    stack = []
    stack.append((start,end,bit,cnt))

    while stack :
        x, y, alphabet, count = stack.pop()
        max_cnt = max(max_cnt, count)

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c :
                bit = 1 << (ord(graph[nx][ny]) - ord('A'))
                if not (alphabet & bit) and visited[nx][ny] != (alphabet | bit) : # 중복 알파벳경로 제외하기위한 visited
                    stack.append((nx,ny, alphabet | bit, count+1))
                    visited[nx][ny] = alphabet | bit

    return max_cnt


bit = 1 << (ord(graph[0][0]) - ord('A'))
print(dfs(0, 0, visited, bit, 1))

# 아래는 재귀함수로 하는 방법
# def dfs(x, y, start_bit, cnt) :
#     max_cnt = cnt
#
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < r and 0 <= ny < c and (nx,ny)  :
#             bit = 1 << (ord(graph[nx][ny]) - ord('A'))
#             if not (start_bit & bit) and visited[nx][ny] != (start_bit | bit):
#                 visited[nx][ny] = start_bit | bit
#                 max_cnt = max(max_cnt, dfs(nx, ny, start_bit | bit, cnt+1))
#
#     return max_cnt
#
#
# start_bit = 1 << (ord(graph[0][0]) - ord('A'))
# print(dfs(0, 0, start_bit, 1))