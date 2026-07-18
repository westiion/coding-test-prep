def solution(box, n):
    cnt=1
    for num in box:
        cnt*=num//n
    return cnt
        
    