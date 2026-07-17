def solution(my_string, letter):
    result=[x for x in my_string if x != letter]
    return ''.join(result)