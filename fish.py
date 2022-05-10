A = [4,3,2,1,5]
B = [0,1,0,0,0]
def solution(A, B):
    # count fish
    count = 0
    # only fish moving in opposite directions
    fish = A[0]
    direction = B[0]
    for i in range(len(A)-1):
        if direction == B[i+1]:
            count += 1
        else:
            if A[i] > A[i+1]:
                A[i] = A[i+1]
            else:
                A[i] = A[j]
    # if A[i] > A[i+j] -> A[i] wins
    # if A[i] < A[i+j] -> A[i+j] wins