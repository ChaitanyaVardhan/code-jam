def solve(I):
    sorted_I = sorted(I, key = lambda i: i[1])
    
    sorted_sched = []
    sorted_sched.append('J')
    J_prev_finish_time = sorted_I[0][1]
    for i in range(1, len(sorted_I)):
        if sorted_I[i][0] >= J_prev_finish_time:
            sorted_sched.append('J')
            J_prev_finish_time = sorted_I[i][1]
        else:
            sorted_sched.append('C')

    C_prev_finish_time = -1
    for i in range(len(sorted_sched)):
        if sorted_sched[i]  == "C":
            if sorted_I[i][0] >= C_prev_finish_time:
                C_prev_finish_time = sorted_I[i][1]
            else:
                sorted_sched[i] = 'X'
        else:
            continue

    unsorted_sched = [0] * len(I)
    i = 0
    while i < len(I):
        j = 0
        while j < len(sorted_I):
            if I[i] != sorted_I[j]:
                j +=1
            else:
                unsorted_sched[i] = sorted_sched[j]
                j = len(sorted_I)
        i +=1

    if "X" in unsorted_sched:
        return "IMPOSSIBLE"
    else:
        return ''.join(unsorted_sched)
    
    
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        I = []
        for _ in range(N):
            m, n = [int(s) for s in input().split(" ")]
            I.append((m,n))
        ans = solve(I)
        print("Case #{}: {}".format(str(i+1), ans))
