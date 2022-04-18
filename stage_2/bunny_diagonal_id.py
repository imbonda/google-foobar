def solution(x, y):
    # Your code here
    if (x, y) == (1, 1):
        return 1
        
    diagonal_num = x + y - 1
    sum_prev_diagonals = int(diagonal_num * (diagonal_num - 1) / 2)
    return str(sum_prev_diagonals + x)
    


tests = [(1,1), (3,2), (2,3), (5,10)]
for t in tests:
    print(solution(*t))