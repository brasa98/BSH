import hashlib, os
import brc
EXC = (".jpg", ".mp3")

""" TODO:
    >Arrumar a escrita do arquivo (\n duplo) --OK
    >Criptografia de diretório SEM RECURSÃO --OK
    >Consertar a perda dos acentos ao usar a cifra de césar --NÃO VAI ROLAR KKKKKK
    >Criar uma função especificamente para (des)criptografar os arquivos (remover todos os elseif's) --OK
    >Consertar os parágrafos "\n" e os duplos parágrafos no começo do arquivo
"""

def lerArquivo(arquivo, modo: str):
    if modo == "r":
        with open(arquivo, "r", encoding='utf-8') as a:
            return a.readlines() if not None else ""
    elif modo == "r1":
        with open(arquivo, "r", encoding='utf-8') as a:
            return a.readline() if not None else []

limparArquivo = lambda arquivo: os.system(f"rm '{arquivo}'")

def criptografarArquivo(nomea: str):
    ARQCHAVE: str = nomea.split(".")[0] + ".brchave"
    path_ARQCHAVE: str = os.getcwd() + "/" + ARQCHAVE

    """
    if ARQCHAVE in os.listdir(): 
        descriptografarArquivo(nomea)
        return
    """
    chave = input("Digite a chave: ")
    
    with open(ARQCHAVE, "w") as a:
        a.write(hashlib.sha512(chave.encode()).hexdigest())
        os.system(f"chmod 444 '{path_ARQCHAVE}'")

    linhas: list[str] | str = lerArquivo(nomea, "r")
    limparArquivo(nomea)
    m = int(input("\nTipo de criptografia:\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
    if m == 3: s = int(input("Digite o deslocamento: "))
    elif m == 4: s = input("Digite a seed: ")

    for linha in linhas:
        with open(nomea, "a") as a:
            if m == 1: a.write(linha[::-1])
            elif m == 2: a.write(brc.binit(linha))
            elif m == 3: a.write(brc.shift(linha, s))
            elif m == 4: a.write(brc.misturar(linha, s))


def descriptografarArquivo(nomea: str):
    ARQCHAVE: str = nomea.split(".")[0] + ".brchave"
    real_chave = lerArquivo(ARQCHAVE, "r1")

    chave = input("Digite a chave para descriptografar: ")
    if hashlib.sha512(chave.encode()).hexdigest() == real_chave:
        m = int(input("\nQual era o método de criptografia?\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
        linhas: list[str] | str = lerArquivo(nomea, "r")

        o = int(input("\nEscolha:\n1-Exibir o arquivo\n2-Descriptografar o arquivo\n=>"))

        if m == 1:
            if o == 1: # Exibir conteúdo do arquivo descriptografado
                for linha in linhas: print(linha[::-1], end='')
            elif o == 2: # Descriptografar o arquivo
                with open(nomea, "a") as a:
                    for linha in linhas:
                        a.write(linha[::-1])
        elif m == 2:
            if o == 1:
                for linha in linhas: print(brc.unbinit(linha), end='')
            elif o == 2:
                with open(nomea, "a") as a:
                    for linha in linhas:
                        a.write(brc.unbinit(linha))
        elif m == 3:
            s = int(input("Qual era o deslocamento? "))
            rev = 26 - s
            if o == 1:
                for linha in linhas: print(brc.shift(linha, rev), end='')
            elif o == 2:
                with open(nomea, "a") as a:
                    for linha in linhas:
                        a.write(brc.shift(linha, rev))

        elif m == 4:
            s = input("Qual era a seed? ")
            if o == 1:
                for linha in linhas: print(brc.desmisturar(linha, s), end='')
            elif o == 2:
                with open(nomea, "a") as a:
                    for linha in linhas:
                        a.write(brc.desmisturar(linha, s))
    else: print("Chave errada, espião.\nNão é legal mexer nas coisas dos outros! Porque você acha que eu criei um programa de criptografia?")

def criptoRec(path: str, recursive=True):
    ARQCHAVE: str = path + "/.brchave"
    path_ARQCHAVE: str = os.getcwd() + "/" + ARQCHAVE
    if ".brchave" in os.listdir(path):
        descriptoRec(path, recursive=recursive)
        return

    chave = input("Digite a chave: ")
    with open(ARQCHAVE, "w") as a:
        a.write(hashlib.sha512(chave.encode()).hexdigest())
    
    os.system(f"chmod 444 '{path_ARQCHAVE}'")

    m = int(input("\nTipo de criptografia:\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistureba\n=>"))
    if m == 3: s = int(input("Digite o deslocamento: "))
    elif m == 4: s = input("Digite a seed: ")

    if recursive:
        for dir, _, arquivos in os.walk(path):
            if arquivos:
                for arq in arquivos:
                    if arq == ".brchave" or arq.endswith(EXC): continue
                    print(arq)
                    nomea = dir + "/" + arq
                    linhas: list[str] | str | None = lerArquivo(nomea, "r")
                    limparArquivo(nomea)
                    with open(nomea, "a") as a:
                        for linha in linhas:
                            if m == 1: a.write(linha[::-1])
                            elif m == 2: a.write(brc.binit(linha))
                            elif m == 3: a.write(brc.shift(linha, s))
                            elif m == 4: a.write(brc.misturar(linha, s))

    else:
        for dir, _, arquivos in os.walk(path):
            if not arquivos: continue
            if path == dir:
                for arq in arquivos:
                    nomea = dir + "/" + arq
                    if arq == ".brchave" or arq.endswith(EXC): continue
                    linhas: list[str] | str | None = lerArquivo(nomea, "r")
                    limparArquivo(nomea)
                    with open(nomea, "a") as a:
                        for linha in linhas:
                            if m == 1: a.write(linha[::-1])
                            elif m == 2: a.write(brc.binit(linha))
                            elif m == 3: a.write(brc.shift(linha, s))
                            elif m == 4: a.write(brc.misturar(linha, s))


def descriptoRec(path: str, recursive=True):
    ARQCHAVE: str = path + "/.brchave"
    path_ARQCHAVE: str = os.getcwd() + "/" + ARQCHAVE
    real_chave = lerArquivo(ARQCHAVE, "r1")

    chave = input("Digite a chave para descriptografar o diretório: ")
    
    if hashlib.sha512(chave.encode()).hexdigest() == real_chave:
        m = int(input("\nQual era o método de criptografia?\n1-Inverter\n2-Binário\n3-Cifra de césar\n4-Mistura\n=>"))
        if m == 3: s = int(input("Digite o deslocamento que foi usado: "))
        elif m == 4: s = input("Digite a seed que foi usada: ")

        if recursive:
            for dir, _, arquivos in os.walk(path):
                if arquivos:
                    for arq in arquivos:
                        if arq == ".brchave" or arq.endswith(EXC): continue
                        print(arq)
                        nomea = dir + "/" + arq
                        linhas: list[str] | str | None = lerArquivo(nomea, "r") 
                        limparArquivo(nomea)
                        for linha in linhas:
                            with open(nomea, "a") as a:
                                if m == 1: a.write(linha[::-1])
                                elif m == 2: a.write(brc.unbinit(linha))
                                elif m == 3:
                                    rev = 26 - s 
                                    a.write(brc.shift(linha, rev))
                                elif m == 4: a.write(brc.desmisturar(linha, s))
        else:
            for dir, _, arquivos in os.walk(path):
                if not arquivos: continue
                if path == dir:
                    for arq in arquivos:
                        if arq == ".brchave" or arq.endswith(EXC): continue
                        nomea = dir + "/" + arq
                        linhas: list[str] | str | None = lerArquivo(nomea, "r")
                        limparArquivo(nomea)
                        for linha in linhas: 
                            with open(nomea, "a") as a:
                                if m == 1: a.write(linha[::-1])
                                elif m == 2: a.write(brc.unbinit(linha))
                                elif m == 3:
                                    rev = 26 - s
                                    a.write(brc.shift(linha, rev))
                                elif m == 4: a.write(brc.desmisturar(linha, s))
            
        os.system(f"rm -f '{path_ARQCHAVE}'")

    else: print("Chave errada, espião.\nNão é legal mexer nas coisas dos outros! Porque você acha que eu criei um programa de criptografia?")
