def solve(I):
    unsorted_sched_1 = solve_for_first(I, 'J', 'C')
    unsorted_sched_2 = solve_for_first(I, 'C', 'J')
    if "X" in unsorted_sched_1 and "X" in unsorted_sched_2:
        return "IMPOSSIBLE"
    elif "X" in unsorted_sched_1:
        return ''.join(unsorted_sched_2)
    else:
        return ''.join(unsorted_sched_1)
    

def solve_for_first(I, parent, other):
    unsorted_sched = []
    unsorted_sched.append(parent)
    p1_prev_finish_time = I[0][1]
    p1_prev_start_time = I[0][0]
    for i in range(1, len(I)):
        if I[i][0] >= p1_prev_finish_time:
            unsorted_sched.append(parent)
            p1_prev_finish_time = I[i][1]
        elif I[i][1] <= p1_prev_start_time:
            unsorted_sched.append(parent)
            p1_prev_start_time = I[i][0]
        else:
            unsorted_sched.append(other)


    j = 0
    while j < len(unsorted_sched):
        if unsorted_sched[j] == other:
            break
        else:
            j += 1
    if j >= 0 and j < len(unsorted_sched):
        p2_prev_finish_time = I[j][1]
        p2_prev_start_time = I[j][0]
        for k in range(j+1, len(unsorted_sched)):
            if unsorted_sched[k]  == other:
                if I[k][0] >= p2_prev_finish_time:
                    p2_prev_finish_time = I[k][1]
                elif I[k][1] <= p2_prev_start_time:
                    p2_prev_start_time = I[k][0]
                else:
                    unsorted_sched[k] = 'X'
            else:
                continue

    return unsorted_sched
    
    
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
