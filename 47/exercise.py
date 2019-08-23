import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())

c_digits = re.compile(r'[0-9]')
c_lowercase = re.compile(r'[a-z]')
c_uppercase = re.compile(r'[A-Z]')

def validate_password(password):
    global used_passwords
    all_conditions = []

    if 5 < len(password) < 13:
        # p_lenght = True
        all_conditions.append(True)

    if len(c_digits.findall(password)) > 0:
        # p_digits = True
        all_conditions.append(True)

    if len(c_lowercase.findall(password)) > 1:
        # p_lowercase = True
        all_conditions.append(True)

    if len(c_uppercase.findall(password)) > 0:
        # p_uppercase = True
        all_conditions.append(True)

    if len([x for x in PUNCTUATION_CHARS if x in password]) > 0:
        # p_punctuation = True
        all_conditions.append(True)

    if password not in used_passwords:
        # p_notused = True
        all_conditions.append(True)

    # this is the main check
    if len(all_conditions) == 6:
        used_passwords.add(password)
        return True
    else:
        return False