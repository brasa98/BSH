import string, random, hashlib

NUMS  =  string.digits
LETS = string.ascii_letters

first = random.randint(1,2)

def salt_it():
    global first
    salt = ''
    #Gerar o sal
    for i in range(random.randint(8,16) + 1):
        if first == 1:
            salt += random.choice(NUMS)
        else:
            salt += random.choice(LETS)
        first = random.randint(1,2)
    return salt

def hash_it(salt: str, word: str):
    #Hashar a palavra junto com o sal
    salted_word  = word + salt
    hashed_word = hashlib.sha224(salted_word.encode()).hexdigest()
    return hashed_word
