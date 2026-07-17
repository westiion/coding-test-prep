from math import sqrt as sqrt
def solution(n):
    if sqrt(n)==int(sqrt(n)):     
        return 1
    else:
        return 2