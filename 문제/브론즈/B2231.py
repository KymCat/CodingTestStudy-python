n = int(input())
m = list(map(int, str(n)))

result = 0
# for i in range(1, n) :
for i in range(max(0,n - 9*(len(str(n)))), n) :
    if n == i + sum(list(map(int, str(i)))) :
        result = i
        break

print(result)


# max(0,n - 9*(len(str(n))))
# N = 생성자 + (생성자 각 자릿수의 합)
# 각 자릿수의 최대값은 9
# 따라서 for이 시작하는 최소범위는 => N - (9*N의자릿수)
# 그런데 27보다 작은경우는 for문이 음수부터 시작하는 경우가 있으니
# max()함수에서 0과 비교함으로써 이를 해결한다.
# 그런데 for문을 1부터 시작해도 문제는 정답으로 처리된다