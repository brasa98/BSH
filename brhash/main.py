import brhashing

def main():
    o = input("Você quer um sal para usar no hash? ")
    salt_hash = o.lower() == "s"
    if salt_hash:
        salt: str = brhashing.salt_it()
        print(f"Esse é o sal: {salt}")
    else:
        salt = ""
    word: str = input("Digite: ")
    #print(f"{word +  salt}")
    sha = input("Digite o algorítmo: (ex: sha256): ")
    hashed_word =  brhashing.hash_it(salt, word, algo=sha)
    print(hashed_word)

if __name__  ==  "__main__":
    main()
