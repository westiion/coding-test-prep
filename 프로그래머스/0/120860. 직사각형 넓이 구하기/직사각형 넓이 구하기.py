def solution(dots):
    a,b,c,d=sorted(dots,reverse=True)
    return (a[1]-b[1]) * (a[0]-c[0])
        