def compute_a_b(N):
    str_N = str(N)
    str_a_arr = list(str_N)
    for i in range(len(str_a_arr)):
        if str_a_arr[i] == "4":
            str_a_arr[i] = "2"
        else:
            str_a_arr[i] = "0"
    a = int(''.join(str_a_arr))

    str_b_arr = list(str_N)
    for j in range(len(str_b_arr)):
        if str_b_arr[j] == "4":
            str_b_arr[j] = "2"
    b = int(''.join(str_b_arr))

    return (a, b)

            
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        r = compute_a_b(N)
        print("Case #{}: {} {}".format(str(i+1), str(r[0]), str(r[1])))
