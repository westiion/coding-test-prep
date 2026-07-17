def solution(my_string):
    result=''
    for string in my_string:
        if string.islower():
            result+=string.upper()
        else:
            result+=string.lower()
    return result