from unidecode import unidecode

def shift(frase: str, chave: int) -> str:
    resultado = ""

    for caractere in frase:
        if caractere.isalpha():
            inicio = ord('a') if caractere.islower() else ord('A')
            caractere_sem_acento = unidecode(caractere)
            if caractere_sem_acento:
                offset = (ord(caractere_sem_acento[0]) - inicio + chave) % 26
                resultado += chr(offset + inicio)
            else:
                resultado += caractere
        elif caractere.isnumeric():
            resultado += str((int(caractere) + chave) % 10)
        else:
            resultado += caractere
    
    return resultado

binit = lambda frase: ' '.join(format(ord(letra), 'b') for letra in frase)

def isbin(txt: str):
    txt = txt.split()
    try: 
        for s in txt:
            int(s, 2)
        return True
    except ValueError:
        return False

def unbinit(frase: str):
    bins = frase.split()
    txt = ''
    for b in bins:
        txt += chr(int(b, 2))
    return txt

def mixher(frase: str, seed):
    """
    1º: Inverter frase? 0 ou 1
    2º: César na frase? 0 ou 1
    3° e 4º: Deslocamento da cifra (1 a 25)
    5°: Binário
    Exemplo:
        11011 (Binário, inverter e cifra 1)
    """
    seed = str(seed)
    
    if seed[0] == '1': frase = frase[::-1]
    if seed[1] == '1': frase = shift(frase, int(seed[2:4]))
    if seed[4] == '1': frase = binit(frase)
    return frase

def unmixher(frase: str, seed):
    seed = str(seed)
    if isbin(frase):
        if seed[4] == '1': frase = unbinit(frase)
        if seed[1] == '1': frase = shift(frase, 26 - int(seed[2:4]))
        if seed[0] == '1': frase = frase[::-1]
    else:
        if seed[0] == '1': frase = frase[::-1]
        if seed[1] == '1': frase = shift(frase, 26 - int(seed[2:4]))
    return frase
