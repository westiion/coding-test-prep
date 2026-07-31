def solution(numbers):
    dict={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    temp=''
    answer=''
    for ch in numbers:
        temp+=ch
        for key,val in dict.items():
            if temp == key:
                answer+=str(val)
                temp=''
    return int(answer)
    