def solution(my_string, num1, num2):
    string=list(my_string)
    second=string[num2]
    string[num2]=string[num1]
    string[num1]=second
    return ''.join(string)
    
    