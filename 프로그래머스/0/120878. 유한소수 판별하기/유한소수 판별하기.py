def solution(a, b):
    for i in range(2, a+1):
        while b % i == 0 and a % i == 0:
            a = a // i
            b = b // i
    so=''
    for i in range(2,b+1):
        if b%i==0:
            if not [j for j in range(2,i) if i%j==0]:
                so+=str(i)
    if so in '25':
        return 1
    else:
        return 2