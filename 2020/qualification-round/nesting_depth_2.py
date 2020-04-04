LEFT_PAREN = "("
RIGHT_PAREN = ")"


def solve(S):
    result = []
    i = 1
    if int(S[0]) > 0:
        insert_parens(result, int(S[0]), LEFT_PAREN)
        
    result.append(S[0])
    while i < len(S):
        diff = int(S[i]) - int(S[i-1])
        if diff > 0:
            insert_parens(result, diff, LEFT_PAREN)
            result.append(S[i])            
        elif diff < 0:
            insert_parens(result, -diff, RIGHT_PAREN)
            result.append(S[i])
        else:
            result.append(S[i])
        i += 1

    if int(S[-1]) > 0:
        insert_parens(result, int(S[-1]), RIGHT_PAREN)
        
    return ''.join(result)


def insert_parens(result, diff, paren):
    for i in range(diff):
        result.append(paren)


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input()
        ans = solve(S)
        print("Case #{}: {}".format(str(i+1), ans))
