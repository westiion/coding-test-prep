def solution(num, k):
    for n in str(num):
        if n==str(k):
            return str(num).index(n)+1
    return -1   