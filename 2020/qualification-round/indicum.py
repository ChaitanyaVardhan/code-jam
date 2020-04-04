import itertools


def solve(N, K):
    row = [i for i in range(1, N+1)]    
    rows = list(itertools.permutations(row))
    matrices = []
    for step in range(1, N, 2):
        for k in range(len(rows)):
            matrix = []
            matrix.append(rows[k])
            build_matrix(matrix, N, step)
            matrices.append(matrix)

    j = 0
    while j < len(matrices):
        trace = compute_trace(matrices[j])
        if trace == K:
            break
        else:
            j += 1

    if j < len(matrices):
        return ("POSSIBLE", matrices[j])
    else:
        return ("IMPOSSIBLE",)

            
def build_matrix(matrix, N, step):
    if len(matrix) == N:
        return
    
    last_row = matrix[-1]
    new_row = [None] * N


    for i in range(N):            
        new_row[i] = last_row[(i+step) % N]
    matrix.append(new_row)
    build_matrix(matrix, N, step)


def compute_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]

    return trace


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = [int(s) for s in input().split()]
        ans = solve(N, K)
        print("Case #{}: {}".format(str(i+1), ans[0]))
        if ans[0] == "POSSIBLE":
            for j in range(len(ans[1])):
                print(' '.join(str(n) for n in ans[1][j]))
