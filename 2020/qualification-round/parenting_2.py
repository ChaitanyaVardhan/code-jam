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

    
def solve(I):
    intervals = []
    residual_intervals = []
    intervals.append(I[0])
    
    i = 1
    while i < len(I):
        if fits(intervals, I[i]):
            intervals.append(I[i])
        else:
            residual_intervals.append(I[i])
        i += 1

    x_intervals = []
    if len(residual_intervals) > 0:
        x_intervals.append(residual_intervals[0])
        i = 1
        while i < len(residual_intervals):
            if fits(x_intervals, residual_intervals[i]):
                x_intervals.append(residual_intervals[i])
            i += 1
            
    sched = []
    for i in range(len(I)):
        if I[i] in intervals:
            sched.append('J')
        elif I[i] in x_intervals:
            sched.append('C')
    if len(sched) < len(I):
        return "IMPOSSIBLE"
    else:
        return ''.join(sched)

    
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
