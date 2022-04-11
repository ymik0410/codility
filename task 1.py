E = "10:20"
M = "11:00"
def solution(E, M):
    price_entrance = 2
    price_first = 3
    price_successive = 4
    hours = int(M[0:2]) - int(E[0:2])
    minutes = int(M[3:5]) - int(E[3:5])
    if minutes > 0:
        succ_hours = hours
    else:
        succ_hours = hours-1
    res = price_entrance + price_first + price_successive*succ_hours
    return res

print(solution("10:00", "13:21"))
print(solution("10:00", "10:21"))
print(solution("09:42", "11:42"))