def solution(my_string):
    overlap=[]
    result=''
    for ch in my_string:
        if ch not in overlap:
            overlap.append(ch)
            result+=ch
            
    return result