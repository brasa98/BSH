import hashlib, os
import brc
EXC = (".jpg", ".mp3")

""" TODO:
    >Arrumar a escrita do arquivo (\n duplo) --OK
    >Criptografia de diretório SEM RECURSÃO --OK
    >Consertar a perda dos acentos ao usar a cifra de césar --NÃO VAI ROLAR KKKKKK
    >Criar uma função especificamente para (des)criptografar os arquivos (remover todos os elseif's) --ACHO QUE TAMBÉM NÃO VAI ROLAR
"""

def readFile(file, mode: str):
    if mode == "r":
        with open(file, "r", encoding='utf-8') as f:
            return f.readlines() if not None else ""
    elif mode == "r1":
        with open(file, "r", encoding='utf-8') as f:
            return f.readline() if not None else []

clearFile = lambda file: os.system(f"rm '{file}'")

def cryptFile(fname: str):
    KFILE: str = fname.split(".")[0] + ".brkey"
    path_kfile: str = os.getcwd() + "/" + KFILE
    if KFILE in os.listdir(): 
        decryptFile(fname)
        return

    chave = input("Digite a chave: ")
    
    with open(KFILE, "w") as f:
        f.write(hashlib.sha512(chave.encode()).hexdigest())
        os.system(f"chmod 444 '{path_kfile}'")

    linhas: list[str] | str = readFile(fname, "r")
    clearFile(fname)
    m = int(input("\nTipo de criptografia:\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
    for linha in linhas:
        with open(fname, "w") as f:
            if m == 1: f.write(linha[::-1])
            elif m == 2: f.write(brc.binit(linha))
            elif m == 3:
                s = int(input("Digite o deslocamento: "))
                f.write(brc.shift(linha, s))
            elif m == 4:
                s = input("Digite a seed: ")
                f.write(brc.mistureba(linha, s))


def decryptFile(fname: str):
    KFILE: str = fname.split(".")[0] + ".brkey"
    real_key = readFile(KFILE, "r1")

    key = input("Digite a chave para descriptografar: ")
    if hashlib.sha512(key.encode()).hexdigest() == real_key:
        m = int(input("\nQual era o método de criptografia?\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
        linhas: list[str] | str = readFile(fname, "r")

        o = int(input("\nEscolha:\n1-Exibir o arquivo\n2-Descriptografar o arquivo\n=>"))

        if m == 1:
            if o == 1: # Exibir conteúdo do arquivo descriptografado
                for linha in linhas: print(linha[::-1], end='')
            elif o == 2: # Descriptografar o arquivo
                with open(fname, "w") as f:
                    for linha in linhas:
                        f.write(linha[::-1])
        elif m == 2:
            if o == 1:
                for linha in linhas: print(brc.unbinit(linha), end='')
            elif o == 2:
                with open(fname, "w") as f:
                    for linha in linhas:
                        f.write(brc.unbinit(linha))
        elif m == 3:
            s = int(input("Qual era o deslocamento? "))
            rev = 26 - s
            if o == 1:
                for linha in linhas: print(brc.shift(linha, rev), end='')
            elif o == 2:
                with open(fname, "w") as f:
                    for linha in linhas:
                        f.write(brc.shift(linha, rev))

        elif m == 4:
            s = input("Qual era a seed? ")
            if o == 1:
                for linha in linhas: print(brc.unmixher(linha, s), end='')
            elif o == 2:
                with open(fname, "w") as f:
                    for linha in linhas:
                        f.write(brc.unmixher(linha, s))
       

def rCrypt(path: str, recursive=True):
    KFILE: str = path + "/.brkey"
    path_kfile: str = os.getcwd() + "/" + KFILE
    if ".brkey" in os.listdir(path):
        rDecrypt(path, recursive=recursive)
        return

    chave = input("Digite a chave: ")
    with open(KFILE, "w") as f:
        f.write(hashlib.sha512(chave.encode()).hexdigest())
    
    os.system(f"chmod 444 '{path_kfile}'")

    m = int(input("\nTipo de criptografia:\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
    if m == 3: s = int(input("Digite o deslocamento: "))
    elif m == 4: s = input("Digite a seed: ")

    if recursive:
        for dir, _, files in os.walk(path):
            if files:
                for f in files:
                    if f == ".brkey" or f.endswith(EXC): continue
                    print(f)
                    fname = dir + "/" + f
                    linhas: list[str] | str | None = readFile(fname, "r")
                    clearFile(fname)
                    with open(fname, "w") as f:
                        for linha in linhas:
                            if m == 1: f.write(linha[::-1])
                            elif m == 2: f.write(brc.binit(linha))
                            elif m == 3: f.write(brc.shift(linha, s))
                            elif m == 4: f.write(brc.mistureba(linha, s))

    else:
        for dir, _, files in os.walk(path):
            if not files: continue
            if path == dir:
                for f in files:
                    fname = dir + "/" + f
                    if f == ".brkey" or f.endswith(EXC): continue
                    linhas: list[str] | str | None = readFile(fname, "r")
                    clearFile(fname)
                    with open(fname, "w") as f:
                        for linha in linhas:
                            if m == 1: f.write(linha[::-1])
                            elif m == 2: f.write(brc.binit(linha))
                            elif m == 3: f.write(brc.shift(linha, s))
                            elif m == 4: f.write(brc.mistureba(linha, s))


def rDecrypt(path: str, recursive=True):
    KFILE: str = path + "/.brkey"
    path_kfile: str = os.getcwd() + "/" + KFILE
    real_key = readFile(KFILE, "r1")

    chave = input("Digite a chave para descriptografar o diretório: ")
    
    if hashlib.sha512(chave.encode()).hexdigest() == real_key:
        m = int(input("\nQual era o método de criptografia?\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-MixHer\n=>"))
        if m == 3: s = int(input("Digite o deslocamento que foi usado: "))
        elif m == 4: s = input("Digite a seed que foi usada: ")

        if recursive:
            for dir, _, files in os.walk(path):
                if files:
                    for f in files:
                        if f == ".brkey" or f.endswith(EXC): continue
                        print(f)
                        fname = dir + "/" + f
                        linhas: list[str] | str | None = readFile(fname, "r") 
                        clearFile(fname)
                        for linha in linhas:
                            with open(fname, "w") as f:
                                if m == 1: f.write(linha[::-1])
                                elif m == 2: f.write(brc.unbinit(linha))
                                elif m == 3:
                                    rev = 26 - s 
                                    f.write(brc.shift(linha, rev))
                                elif m == 4: f.write(brc.unmixher(linha, s))
        else:
            for dir, _, files in os.walk(path):
                if not files: continue
                if path == dir:
                    for f in files:
                        if f == ".brkey" or f.endswith(EXC): continue
                        fname = dir + "/" + f
                        linhas: list[str] | str | None = readFile(fname, "r")
                        clearFile(fname)
                        for linha in linhas: 
                            with open(fname, "w") as f:
                                if m == 1: f.write(linha[::-1])
                                elif m == 2: f.write(brc.unbinit(linha))
                                elif m == 3:
                                    rev = 26 - s
                                    f.write(brc.shift(linha, rev))
                                elif m == 4: f.write(brc.unmixher(linha, s))
            
        os.system(f"rm -f '{path_kfile}'")

    else: print("Chave errada, espião.\nNão é legal mexer nas coisas dos outros! Porque você acha que eu criei um método de criptografia?")
