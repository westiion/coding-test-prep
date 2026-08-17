str = input()
answ=''
for s in str:
    if s.isupper():
        answ+=s.lower()
    else:
        answ+=s.upper()
print(answ)