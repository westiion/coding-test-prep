def solution(my_string):
    result=[]
    for string in my_string:
        if string.isnumeric():
            result.append(int(string))
    return sorted(result)
            