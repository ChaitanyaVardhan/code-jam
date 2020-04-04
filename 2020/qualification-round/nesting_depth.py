RIGHT_PAREN = ")"
LEFT_PAREN = "("
ZERO = '0'
ONE = '1'

def solve(S):
    result = []
    count = 0
    i = 0
    while i < len(S):
        if S[i] == ZERO and count == 0:
            result.append(S[i])
        elif S[i] == ZERO and count > 0:
            result.append(RIGHT_PAREN)
            result.append(S[i])
            count = 0
        elif S[i] == ONE and count == 0:
            result.append(LEFT_PAREN)
            result.append(S[i])
            count += 1
        elif S[i] == ONE and count > 0:
            result.append(S[i])
            count +=1
        i += 1
    if result[-1] == ONE:
        result.append(RIGHT_PAREN)
        
    return ''.join(result)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input()
        ans = solve(S)
        print("Case #{}: {}".format(str(i+1), ans))
