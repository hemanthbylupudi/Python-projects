import random
import string
def get_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
password = get_random_password(12)
print(password)
