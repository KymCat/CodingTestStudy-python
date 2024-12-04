# 거스름돈 500, 100, 50, 10 동전이 무한히 존재
# 손님에게 거슬러야 할 돈은 N원  ( 단 N은 항상 10의 배수 )
# 거슬러줘야할 동전의 최소개수는 ? --> coin

# 동전의 개수가 최소가 될려면 액수가 큰 동전에서 작은 동전 순으로 줘야함.
N = int(input())
coin = 0
cur = 0 # 나눈 동전스택

for i in (500,100,50,10) :
    cur = N//i
    coin += cur
    N -= i*cur

print(coin)

# # 해설
# N = 1260
# count = 0
#
# # 큰 단위의 화폐부터 차례대로 확인
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types :
#     count += N // coin
#     N %= coin
#
# print(count)
