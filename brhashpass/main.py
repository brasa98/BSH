import brhashing, json as j

FNAME = 'ab_cnffjbeqf_urer.txt'

def main():
    o = input("Você quer um sal para usar no hash? ")
    salt_hash = o.lower() == 's'
    if salt_hash:
        salt: str = brhashing.salt_it()
        print(f"Esse é o sal: {salt}")
    user = input("Usuário: ")
    o = input("Você quer hashar o usuário? ")
    hash_user = o.lower() == 's'
    if hash_user:
        user = brhashing.hash_it(salt, user)

    passwd: str = input("Digite a senha: ")
    print(f"{passwd +  salt}")
    hashed_passwd =  brhashing.hash_it(salt, passwd)
    print(hashed_passwd)

    login_info = {
        'user': user,
        'hash_password': hashed_passwd,
        'salt': salt
    }
    print(login_info)
    with open(FNAME, 'a') as f:
        f.write(j.dumps(login_info) + ',  ')

if __name__  ==  "__main__":
    main()