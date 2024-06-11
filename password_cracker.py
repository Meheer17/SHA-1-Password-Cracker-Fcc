import hashlib

def crack_sha1_hash(hash, use_salts = False):
    with open('top-10000-passwords.txt') as file:
        passwords = file.readlines()
    passwords = [password.strip() for password in passwords]
    if use_salts:
        with open('known-salts.txt') as file:
            salts = file.readlines()
        salts = [salt.strip() for salt in salts]
        for salt in salts:
            for password in passwords:
                salted_password = salt + password
                hashed_password = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed_password == hash:
                    return password
            for password in passwords:
                salted_password = password + salt
                hashed_password = hashlib.sha1(salted_password.encode()).hexdigest()
                if hashed_password == hash:
                    return password
        return "PASSWORD NOT IN DATABASE"
    else:
        for password in passwords:
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            if hashed_password == hash:
                return password
        return "PASSWORD NOT IN DATABASE"