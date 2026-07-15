def solution(n):
    if n<6:
        num=-1
    else:
        num=1
    for i in [1,2,3,6]:
        if (n*i)%6==0:
            return (n*i-1)//6+1
