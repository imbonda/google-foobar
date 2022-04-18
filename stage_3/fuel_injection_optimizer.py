from math import log

def solution(n):
    # Your code here
    num = int(n)
    binary = list(bin(int(num))[2:])
    c = 0
    i = len(binary)-1
    while i > 0:
        b = binary[i]
        if b == '0':
            # Devide by 2
            c += 1
            i -= 1
        elif i == 1:
            c += 2
            i -= 2
        else:
            ones = 0
            j = i
            while binary[j] == '1' and j >= 0:
                ones += 1
                j -= 1
            
            c += ones + 1
            i = j
            if ones > 1:
                binary[i] = '1'

    return c

        

def solution_recursive(n):
    # Your code here
    n = int(n)
    if n in (1, 2, 3):
        return n - 1
    
    log2 = log(n, 2)
    if log2.is_integer():
        return int(log2)
        
    if n % 2 == 0:
        return 1 + solution(n // 2)
    return min(
        2 + solution((n - 1) // 2),
        2 + solution((n + 1) // 2)
    )
        


test_cases = [1, 2, 3, 4, 5, 15, 123124123411123123123812381283812378127312221, int('2'*300)]
for t in test_cases:
    print (f'num - {t}:', solution(t), solution_recursive(t))
