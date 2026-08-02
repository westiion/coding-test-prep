def solution(my_string):
    my_string=my_string.split(' ')
    total=int(my_string[0])
    for i in range(2,len(my_string),2):
        if my_string[i-1] == '+':
            total+=int(my_string[i])
        else:
            total-=int(my_string[i])
    return total