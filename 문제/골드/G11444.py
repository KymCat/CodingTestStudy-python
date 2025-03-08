import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
dp = defaultdict(int)
dp[0],dp[1],dp[2] = 0,1,1
def fibonacci(num) :
    if num <= 2 :
        return dp[num]

    elif dp[num] :
        return dp[num]

    else :
        half = num//2
        if num % 2 == 0 :
            fn = fibonacci(half)
            fn_1 = fibonacci(half - 1)
            f2n = fn * (2*fn_1 + fn)
            dp[num] = f2n % 1_000_000_007

        else :
            fn = fibonacci(half + 1)
            fn_1 = fibonacci(half)
            f2n_1 = fn_1**2 + fn**2
            dp[num] = f2n_1 % 1_000_000_007

        return dp[num]


print(fibonacci(n))
