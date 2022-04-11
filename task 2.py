def solution(N):
    count = 0
    while N%2 == 0:
        count += 1
        N = N/2
    return count

print(solution(24))