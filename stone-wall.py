H = [2,5,1,4,6,7,9,10,1]
T = [2,5,1,4,6,7,9,10]
A = []

def solution(H):
    Q = []
    count = 0
    if len(H) > 0:
        Q.append(H[0])
        count += 1
        for i in range(1, len(H)):
            if H[i] > Q[-1]:
                count += 1
                Q.append(H[i])
            elif H[i] < Q[-1]:
                while Q and H[i] < Q[-1]:
                    Q.pop()
                if H[i] not in Q:
                    count += 1
                    Q.append(H[i])
    return count

print(solution(H))
print(solution(T))
print(solution(A))
