def solve(I):
    unsorted_sched = []
    unsorted_sched.append('J')
    J_prev_finish_time = I[0][1]
    J_prev_start_time = I[0][0]
    for i in range(1, len(I)):
        if I[i][0] >= J_prev_finish_time:
            unsorted_sched.append('J')
            J_prev_finish_time = I[i][1]
        elif I[i][1] < J_prev_start_time:
            unsorted_sched.append('J')
            J_prev_start_time = I[i][0]
        else:
            unsorted_sched.append('C')

    C_prev_finish_time = -1
    C_prev_start_time = -2
    for i in range(len(unsorted_sched)):
        if unsorted_sched[i]  == "C":
            if I[i][0] >= C_prev_finish_time:
                C_prev_finish_time = I[i][1]
            elif I[i][1] < C_prev_start_time:
                C_prev_start_time = I[i][0]
            else:
                unsorted_sched[i] = 'X'
        else:
            continue

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
