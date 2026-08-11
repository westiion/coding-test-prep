def solution(n):
    temp=0
    for _ in range(n):
        temp+=1
        while '3' in str(temp) or temp%3==0:
            temp+=1
    return temp