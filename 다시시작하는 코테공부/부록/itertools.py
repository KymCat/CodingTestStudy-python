import itertools
print(list(itertools.permutations([1, 2, 3]))) # 리스트 가능한 모든 순열 출력
print(list(itertools.combinations([1, 2, 3], 2))) # 2개를 뽑는 모든 조합, 순서 고려 X
print(list(itertools.product([1, 2, 3], repeat = 2))) # 2개를 뽑는 모든 조합, 순서고려 O, 중복 허용
print(list(itertools.combinations_with_replacement([1, 2, 3], 2))) # combinations에서 중복허용