def solution(n: int) -> int:
    if n <= 0:
        return -1  # Invalid input

    dp = [0] * n
    dp[0] = 1

    p2 = p3 = p5 = 0

    for i in range(1, n):
        a = dp[p2] * 2
        b = dp[p3] * 3
        c = dp[p5] * 5

        dp[i] = min(a, b, c)

        if dp[i] == a:
            p2 += 1
        if dp[i] == b:
            p3 += 1
        if dp[i] == c:
            p5 += 1

    return dp[n - 1]



if __name__ == "__main__":
    n = int(input())
    print(solution(n))
