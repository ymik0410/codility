A = [3,4,3,2,3,-1,3,3]

def solution(A):
    # write your code in Python 3.6
    leader_index = -1
    if len(A) > 0:
        A_not_sorted = A.copy()
        A.sort()    
        n = len(A)//2
        candidate = A[n]
        frequency = 0
        for i in range(len(A)):
            if A[i] == candidate:
                frequency += 1
        if frequency > n:
            leader_index = A_not_sorted.index(A[n])
    return leader_index

print(solution(A))
