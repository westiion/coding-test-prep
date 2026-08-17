def solution(n_str):
    answer=''
    still_zero=True
    for string in n_str:
        if string == '0':
            if still_zero:
                pass
            else:
                answer+=str(string)
        else:
            answer+=str(string)
            still_zero=False
    return answer
                
    return answer