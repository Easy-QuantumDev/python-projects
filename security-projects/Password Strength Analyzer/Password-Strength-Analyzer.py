import re
from collections import Counter

def is_common_password(psw):
    common = ["password", "123456", "qwerty", "abc123", "password1", "letmein"]
    return psw.lower() in [p.lower() for p in common]
def estimate_time_to_crack(psw):
    if len(psw)<= 4 :
        return 'less than 1 second '
    charset = set(psw)
    charset_size = len(charset)
    if charset_size <= 10 :
        return 'between one to two minutes'
    elif charset_size <= 36 :
        return f'{psw} between one year'
    else:
        return 'impossible'
def get_strength(psw):
    score = 0
    length = len(psw)
    if length >= 12:
        score += 25
    elif length >= 8:
        score += 15
    elif length >= 4:
        score += 5
    if re.search(r'[A-Z]',psw): score+=20
    if re.search(r'\d', psw): score += 15
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', psw): score += 15
    counter = Counter(psw)
    max_repeat = max(counter.values())
    if max_repeat >=length // 2 : score -=10

    if score >=75:
        return f'{psw} is a perfect password to use'
    elif score >=50:
        return f'{psw} is a normal password to use'
    else:
        return f'{psw} is a bad and weak password to use'
def main():
    print('a simple password analyzer with python')
    while True:
        password= input("please enter your password :")
        if not password:
            print("please enter a password")
        break
    print("\n" ,'=' * 50)
    print(f'password : {password}')
    print(f'progressing.... {get_strength(password)}')
    print(f'time to break {estimate_time_to_crack(password)}')
    if is_common_password(password):
        print('the password is in common password list and this is easy to crack')

main()

