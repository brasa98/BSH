import string, random, hashlib

NUMS  =  string.digits
LETS = string.ascii_letters

first = random.randint(1,2)

def salt_it():
    global first
    salt = ''
    #Gerar o sal
    for _ in range(random.randint(8,16) + 1):
        if first == 1:
            salt += random.choice(NUMS)
        else:
            salt += random.choice(LETS)
        first = random.randint(1,2)
    return salt

def hash_it(salt: str, word: str, algo='sha224'):
    hashed_word = ''
    #Hashar a palavra junto com o sal
    salted_word  = word + salt
    match algo:
        case 'sha1':
            hashed_word = hashlib.sha1(salted_word.encode()).hexdigest()
        case 'sha224':
            hashed_word = hashlib.sha224(salted_word.encode()).hexdigest()
        case 'sha256':
            hashed_word = hashlib.sha256(salted_word.encode()).hexdigest()
        case 'sha384':
            hashed_word = hashlib.sha384(salted_word.encode()).hexdigest()
        case 'sha512':
            hashed_word = hashlib.sha512(salted_word.encode()).hexdigest()
        case _:
            hashed_word = hashlib.sha224(salted_word.encode()).hexdigest()
    return hashed_word
