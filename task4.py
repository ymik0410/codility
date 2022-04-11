def solution(A):
    # write your code in Python 3.6
    pass
    n = max(A)
    min_set = 0
    if n<1:
        return 1
    else:
        my_set = set(range(1, n))
        for num in A:
            if num in my_set:
                my_set.remove(num)
    if my_set == set():
        return(n+1)
    else:
        return(min(my_set))

A = [1,3,6,4,2,1]
print(solution(A))