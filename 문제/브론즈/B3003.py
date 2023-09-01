chess_set = [1,1,2,2,2,8]
my_set = list(map(int, input().split()))

for i in range(len(chess_set)) :
    print(chess_set[i] - my_set[i], end=" ")