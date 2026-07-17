def solution(my_string):
    my_string=list(my_string)
    result=list(filter(lambda x : x not in ['a','e','i','o','u'],my_string))
    return ''.join(result)