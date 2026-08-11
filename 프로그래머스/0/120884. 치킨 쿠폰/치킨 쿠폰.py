def solution(chicken):
    coupon=chicken
    result=0
    while coupon >= 10:
        service=coupon//10
        result+=service
        coupon=coupon%10 + service
    return result