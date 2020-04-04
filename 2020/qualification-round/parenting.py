def solve(I):
    unsorted_sched_1 = solve_for_first(I, 'J', 'C')
    unsorted_sched_2 = solve_for_first(I, 'C', 'J')
    if "X" in unsorted_sched_1 and "X" in unsorted_sched_2:
        return "IMPOSSIBLE"
    elif "X" in unsorted_sched_1:
        return ''.join(unsorted_sched_2)
    else:
        return ''.join(unsorted_sched_1)
    

def fits(intervals, elem):
    temp_arr = list(intervals)
    temp_arr.append(elem)
    if non_overlapping(temp_arr):
        return True
    else:
        return False
    

def non_overlapping(interval_arr):
    sorted_arr = sorted(interval_arr, key=lambda x: x[1])
    i = 0
    while i < len(interval_arr)-1:
        if sorted_arr[i][1] <= sorted_arr[i+1][0]:
            i += 1
        else:
            break

    if i == len(sorted_arr) - 1:
        return True
    else:
        return False

    
def solve_for_first(I, parent, other):
    sched = []
    sched.append(parent)
    intervals = []
    intervals.append(I[0])
    
    i = 1
    while i < len(I):
        if fits(intervals, I[i]):
            sched.append(parent)
            intervals.append(I[i])
        else:
            sched.append("X")
        i += 1
        
    residual_intervals = []
    for k in range(1, len(sched)):
        if sched[k] == "X":
            residual_intervals.append(I[k])
        else:
            continue

    if non_overlapping(residual_intervals):
        for j in range(len(sched)):
            if sched[j] == "X":
                sched[j] = other
            else:
                continue
            
    return sched
    
    
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
