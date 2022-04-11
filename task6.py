A = [-3, -1,-2,-2,-5, -6]

def solution(A):
    if len(A)==3:
        return A[0]*A[1]*A[2]
    else:
        A.sort()
        max1 = A[len(A)-1]
        max2 = A[len(A)-2]
        max3 = A[len(A)-3]
        min_1 = A[0]
        min_2 = A[1]
        if max1 < 0:
            return(max1*max2*max3)
        if min_1*min_2 > max1*max2:
            return(min_1*min_2*max1)
        else:
            return(max1*max2*max3)

print(solution(A))
