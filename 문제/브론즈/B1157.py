# from collections import Counter
#
# str = input().upper()
# cnter = Counter(str)
# cnt = list(cnter.values())
# if cnt.count(max(cnt)) >= 2 :
#     print('?')
# else :
#     print(cnter.most_common(1)[0][0]) => 생각보다 느렸음

str = input().upper()
word_list = list(set(str)) # set은 중복을 허용하지 않아서 중복문자 모두 제거

cnt = []
for i in word_list : # 리스트.count()로 각 단어들의 개수 파악
    cnt.append(str.count(i))

if cnt.count(max(cnt)) > 1 :
    print('?')
else :
    print(word_list[cnt.index(max(cnt))])
# word_lst = > ['a', 'b', 'c', 'd']
# cnt      = > [ 1 ,  2 ,  5,   3]
# cnt에서 가장 큰 수를 가지고 있는 인덱스를 찾는다.