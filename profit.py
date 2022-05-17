A = [23171, 21011, 21123, 21366, 21013, 21367]
B = [5, -7, 3, 5, -2, 4, -1]
C = [5]

# Solution Complexity O(n^2) - max profit problem
def solution(A):
    result = 0
    n = len(A)
    for p in range(n):
        sub = 0
        for q in range(p, n):
            sub = A[q]- A[p]
            result = max(result, sub)
    return result

# Solution Complexity O(n) - max slice problem
 
def solution_max_slice(A):
    sum = 0
    max_sum = 0
    for a in A:
        sum += a
        sum = max(sum, 0)
        max_sum = max(sum, max_sum)
    return max_sum

# Solution Complexity O(n) - max profit problem
def solution_max_profit(A):
    profit = 0
    max_profit = 0
    if len(A) > 1:
        profit = 0
        for i in range(1, len(A)):
            added_profit = A[i] - A[i-1]
            profit = max(profit + added_profit, 0)
            max_profit = max(max_profit, profit)
    return max_profit
