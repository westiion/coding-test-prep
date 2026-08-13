def solution(num_list):
    gop=1
    for num in num_list:
        gop*=num
    return 0 if gop>sum(num_list)**2 else 1