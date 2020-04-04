import itertools


def solve(N, K):
    row = [i for i in range(1, N+1)]    
    rows = list(itertools.permutations(row))
    matrices = []
    for i in range(len(rows)):
        matrix = []
        matrix.append(rows[i])
        build_matrix(matrix, N)
        matrices.append(matrix)

    while i < len(matrices):
        trace = compute_trace(matrices[i])
        if trace == K:
            break
        else:
            i += 1

    if i < len(matrices):
        return ("POSSIBLE", matrices[i])
    else:
        return ("IMPOSSIBLE",)

            
def build_matrix(matrix, N):
    if len(matrix) == N:
        return
    
    last_row = matrix[-1]
    new_row = [None] * N
    for i in range(N):
        new_row[i] = last_row[(i+1) % N]
    matrix.append(new_row)
    build_matrix(matrix, N)


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
            for i in range(len(ans[1])):
                print(' '.join(str(n) for n in ans[1][i]))
