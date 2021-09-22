textos = [
    "Mãe tem café?",
    "Bom dia meu bem",
    "Vamos assistir um filme",
    "Meu povo o cuscuz ta pronto",
    "O ciúme é a incerteza da certeza de que você é amado",
    "Me lembrei de você"
]

for texto in textos:
    mensagem = ""
    maior_len = ""
    i = 0
    x = texto.split(" ")

    while i < len(x):
        mensagem += str(len(x[i])) + "-"
        if len(x[i]) > len(maior_len):
            maior_len = x[i]

        i += 1

    mensagem = mensagem[-len(mensagem):-1]
    print("{:25s} {}".format(mensagem, maior_len))