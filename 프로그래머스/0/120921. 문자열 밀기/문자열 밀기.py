def solution(A, B):
    cnt=0
    while True:
        if A == B:
            return cnt
        else:
            cnt+=1
            A = A[-1] + A[:-1]
        if cnt>len(A):
            return -1
        