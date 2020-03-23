def compute_a_b(N):
    n = N - 1
    while n > 0:
        a = n
        b = N - n
        if has_digit_4(a, b):
            n -= 1
        else:
            break

    return (a, b)


def has_digit_4(a, b):
    str_a = str(a)
    str_b = str(b)
    
    i = 0
    while i < len(str_a):
        if str_a[i] == "4":
            break
        else:
            i += 1
    if i < len(str_a):
        return True

    j = 0
    while j < len(str_b):
        if str_b[j] == "4":
            break
        else:
            j += 1
    if j < len(str_b):
        return True

    return False


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        r = compute_a_b(N)
        print("Case #{}: {} {}".format(str(i+1), str(r[0]), str(r[1])))
