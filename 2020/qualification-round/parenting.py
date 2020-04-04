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
        elif I[i][1] < p1_prev_start_time:
            unsorted_sched.append(parent)
            p1_prev_start_time = I[i][0]
        else:
            unsorted_sched.append(other)

    p2_prev_finish_time = -1
    p2_prev_start_time = -2
    for i in range(len(unsorted_sched)):
        if unsorted_sched[i]  == other:
            if I[i][0] >= p2_prev_finish_time:
                p2_prev_finish_time = I[i][1]
            elif I[i][1] < p2_prev_start_time:
                p2_prev_start_time = I[i][0]
            else:
                unsorted_sched[i] = 'X'
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
