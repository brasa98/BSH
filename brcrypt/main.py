import brcfile, brc

o = int(input("brcrypting\n\n1-Criptografia\n2-Criptografia de arquivos\n3-Descriptografar\n=>"))

if o == 1: # Criptografia
    o = int(input("\nMétodo:\n1-Binário\n2-Cifra de César\n3-MixHer\n=>"))
    if o == 1:
        b = brc.binit(input("Digite: "))
        print(b)
    elif o == 2:
        c = brc.shift(input("Digite a frase: "), int(input("Digite o deslocamento: ")))
        print(c)
    elif o == 3:
        sc = brc.mixher(input("Digite a frase: "), input("Digite a seed: "))
        print(sc)

elif o == 2: # Criptografia de Arquivos
    o = int(input("\nUm arquivo único ou um diretório? <1; 2> "))
    if o == 1:
        file = input("Digite o nome do arquivo: ")
        brcfile.cryptFile(file)
    elif o == 2:
        path = input("Caminho para o diretório: ")
        if not path: path = '.'
        r = input("Recursivo? <s; n> ")
        r = True if r.lower() == 's' else False
        brcfile.rCrypt(path, recursive=r)

elif o == 3: # Descriptografia
    o = int(input("\nMétodo:\n1-Binário\n2-Cifra de César\n3-MixHer\n=>"))
    if o == 1:
        b = brc.unbinit(input("Digite: "))
        print(b)
    elif o == 2:
        c = brc.shift(input("Digite a frase: "), 26 - int(input("Digite o deslocamento: ")))
        print(c)
    elif o == 3:
        sc = brc.unmixher(input("Digite a frase: "), input("Digite a seed: "))
        print(sc)
