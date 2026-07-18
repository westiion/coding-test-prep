def solution(cipher, code):
    lst=[cipher[i*code-1] for i in range(1,len(cipher)//code+1)]
    return ''.join(lst)