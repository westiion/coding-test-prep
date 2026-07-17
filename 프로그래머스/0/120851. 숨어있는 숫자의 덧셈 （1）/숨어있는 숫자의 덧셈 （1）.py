def solution(my_string):
    total=0
    for string in my_string:
        if string.isnumeric():
            total+=int(string)
    return total