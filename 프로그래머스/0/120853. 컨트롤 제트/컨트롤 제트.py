def solution(s):
    prev=''
    total=0
    s=s.split(' ')
    for ch in s:
        if ch == 'Z':
            total-=int(prev)
        else:
            total+=int(ch)
        prev=ch
    return total