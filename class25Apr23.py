
commonPasswds = [
    '123456',
    '123456789',
    'qwerty',
    'password',
    '12345',
    'qwerty123',
    '1q2w3e',
    '12345678',
    '111111',
    '1234567890'
]

def passwordPrompt():
    passwd = input("Pick a password: \n")

    if passwd in commonPasswds:
        print("ERROR: Password is commonly used. Please pick a different password.\n\n")

        return passwordPrompt()

    else:
        return passwd


passwd = passwordPrompt()
print(f"Selected password is {passwd}")
