def solution(n):
    result=[]
    temp=[]
    for i in range(2,n+1):
        temp=[]
        for j in range(2,i+1):
            if i%j==0:
                temp.append(j)
        if len(temp)==1 and n%i==0:
            result.append(i)
    return result
    