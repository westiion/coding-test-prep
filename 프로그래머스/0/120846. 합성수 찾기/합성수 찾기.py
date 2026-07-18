def solution(n):
    total_cnt=0
    for i in range(1,n+1):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt>=3:
            total_cnt+=1
    return total_cnt