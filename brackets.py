S = "{[()()]}"
T = "]"

def solution(S):
    L = []
    for br in S:
        if br == "{" or br == "(" or br == "[":
            L.append(br)
        elif len(L) > 0:
            if br == "}" and L[-1] == "{":
                L.pop()
            elif br == "]" and L[-1] == "[":
                L.pop()
            elif br == ")" and L[-1] == "(":
                L.pop()
        else: 
            return 0
    return 1 if len(L) == 0 else 0
