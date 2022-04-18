def solution(l):
    # Your code here
    def version_cmp(a, b):
        a, b = a.split('.'), b.split('.')
        n = len(b)
        
        for i, a_v_num in enumerate(a):
            if i >= n:
                return 1
            
            a_v_num = int(a_v_num)
            b_v_num = int(b[i])
            if a_v_num < b_v_num:
                return -1
            elif b_v_num < a_v_num:
                return 1
        
        if i < n:
            return -1
        return 0
    
    l.sort(cmp=version_cmp)
    return l


l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print(solution(l))
print(l)