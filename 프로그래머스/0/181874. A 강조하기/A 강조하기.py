def solution(myString):
    answer=''
    for str in myString.replace('a','A'):
        if str.isupper():
            if str != 'A':
                answer+=str.lower()
            else:
                answer+=str
        else:
            answer+=str      
    return answer