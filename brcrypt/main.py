import brcfile, brc

o = int(input("brcrypt\n\n1-Criptografar\n2-Criptografar Arquivos\n3-Descriptografar\n4-Descriptografar Arquivos\n=>"))

if o == 1: # Criptografar
    o = int(input("\nMétodo:\n1-Binário\n2-Cifra de César\n3-Misturar\n=>"))
    if o == 1:
        b = brc.prabin(input("Digite a frase: "))
        print(b)
    elif o == 2:
        c = brc.shift(input("Digite a frase: "), int(input("Digite o deslocamento: ")))
        print(c)
    elif o == 3:
        sc = brc.misturar(input("Digite a frase: "), input("Digite a seed: "))
        print(sc)

elif o == 2: # Criptografar Arquivos
    o = int(input("\nUm arquivo único ou um diretório? <1; 2> "))
    if o == 1:
        file = input("Digite o nome do arquivo: ")
        brcfile.criptografarArquivo(file)
    elif o == 2:
        caminho = input("Caminho para o diretório: ")
        if not caminho: caminho = '.'
        r = input("Recursivo? <s; n> ")
        r = True if r.lower() == 's' else False
        brcfile.criptoRec(caminho, recursive=r)

elif o == 3: # Descriptografar
    o = int(input("\nMétodo:\n1-Binário\n2-Cifra de César\n3-Misturar\n=>"))
    if o == 1:
        b = brc.desbin(input("Digite a frase: "))
        print(b)
    elif o == 2:
        c = brc.shift(input("Digite a frase: "), 26 - int(input("Digite o deslocamento: ")))
        print(c)
    elif o == 3:
        sc = brc.desmisturar(input("Digite a frase: "), input("Digite a seed: "))
        print(sc)

elif o == 4: # Descriptografar Arquivos
    o = int(input("\nUm arquivo único ou um diretório? <1; 2> "))
    if o == 1:
        file = input("Digite o nome do arquivo: ")
        brcfile.descriptografarArquivo(file)
    elif o == 2:
        caminho = input("Caminho para o diretório: ")
        if not caminho: caminho = '.'
        r = input("Recursivo? <s; n> ")
        r = True if r.lower() == 's' else False
        brcfile.descriptoRec(caminho, recursive=r)