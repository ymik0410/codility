A = [10, 2, 5, 1, 8, 20]
B = [-1]
'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
'''

def solution(A):
    # if there is a triangle, return 1
    # else, return 0
    
    A.sort()
    i = 0
    while i < len(A) and A[i] < 0:
        i+=1
    for p in range(i, len(A)-2):
        for q in range(p+1, len(A)-1):
            x = A[p]
            y = A[q]
            z = A[q+1]
            
            if x+y > z:
                return 1
    return 0
        
print(solution(A))
print(solution(B))
