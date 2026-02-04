import string


def checker(password):
    answer = True
    if len(password) < 6:
        print(f"Too Few Characters in “{password}”! At Least 6 Characters.")
        answer = False

    if len(password) > 12:
        print(f"Too Many Characters in “{password}”! At Most 12 Characters.")
        answer = False

    if not any(c.isdigit() for c in password):
        print(f"No Numbers Found in “{password}”! At Least 1 Number(0-9).")
        answer = False

    if not any(c.isupper() for c in password):
        print(f"No Uppercase Characters Found in “{password}”! At Least 1 Uppercase Character. (A-Z)")
        answer = False

    if not any(c.islower() for c in password):
        print(f"No Lowercase Characters Found in “{password}”! At Least 1 lowercase Character. (a-z)")
        answer = False

    if not any(c in string.punctuation for c in password):
        print(f"No Special Characters Found in “{password}”! At Least 1 Special Character. (!@#$%)")
        answer = False

    return answer


password = input("Enter The Password:")

if checker(password):
    print(f"{password} is Valid.")
