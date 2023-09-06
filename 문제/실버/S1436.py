# 브루트 포스 문제
# 솔직히 문제 이해하기 너무 어렵다
# 666,1666,2666,3666,4666,5666,6660
# 6666 보다 6660이 작기 때문에 7 번째 영화는 6660이다.

n = int(input())
cnt = 0
start = 666

while True :
    if '666' in str(start) :
        cnt+=1

    if cnt == n :
        print(start)
        break

    start +=1


# N = int(input()) => 40ms 훨씬 빠름
# li = []
# n = 0
# while len(li) < N:
#     if not n%10 == 6:
#         li.append(n*1000+666)
#     elif (n//10)%100 == 66:
#         for k in range (1000):
#             li.append(n*1000+k)
#     elif (n//10)%10 == 6:
#         for j in range (100):
#             li.append(n*1000+600+j)
#     else:
#         for i in range (10):
#             li.append(n*1000+660+i)
#     n += 1
#
# print (li[N-1])