def solution(i, j, k):
    cnt=0
    for x in range(i,j+1):
        cnt+=str(x).count(str(k))
    return cnt
    