def solution(arr, intervals):
    l,r=intervals
    a,b=l
    c,d=r
    return arr[a:b+1]+arr[c:d+1]