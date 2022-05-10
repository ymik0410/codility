S = "("
T = ")"
U = "(())()()"

def solution(S):
    # return 0 if not properly nested
    # return 1 if properly nested
    L  = []
    for i in range(len(S)):
        if S[i] == "(":
            L.append(S[i])
        elif len(L) > 0 and L[-1] == "(":
            L.pop()
        else:
            return 0
    return 1 if len(L) == 0 else 0

print(solution(S)) 
print(solution(T))      
print(solution(U))
        