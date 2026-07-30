def solution(balls, share):
    answer=factorial(balls)/(factorial(balls-share)*factorial(share))
    return answer

def factorial(x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)