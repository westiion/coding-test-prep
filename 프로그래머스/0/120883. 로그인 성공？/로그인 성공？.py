def solution(id_pw, db):
    result='fail'
    for id, pw in db:
        if id in id_pw:
            result='wrong pw'
            if pw in id_pw:
                result='login'
    return result
            
        
    