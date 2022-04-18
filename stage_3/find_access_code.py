def solution(l):
    # Your code here
    ans = 0
    
    for i, y in enumerate(l):
        x_count = 0
        z_count = 0
        for j, w in enumerate(l):
            if j == i:
                continue
            elif j < i and y % w == 0:
                x_count += 1
            elif j > i and w % y == 0:
                z_count += 1
        ans += x_count * z_count
    
    return ans


tests = [
    [1,2,3,4,5,6],
    [1,1,1]
]
for t in tests:
    print(f'testing {t}, result:\t', solution(t))