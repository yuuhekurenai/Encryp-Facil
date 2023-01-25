alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

texto_usuario = input("digite 'encode' para criptografar, digite 'decode' para descriptogafar:\n")
texto = input("Escreva sua mensagem:\n").lower()
troca = int(input("Digite um numero para a criptografia:\n"))


def encrypt(plan_texto, qtd_troca):
    criptografia = ""
    for letras in plan_texto:
        posicao = alfabeto.index(letras)
    nova_posicao = posicao + qtd_troca
    nova_letra = alfabeto[nova_posicao]
    criptografia += nova_letra
    print(f"A criptografia será: {criptografia}")


def decrypt(plan_texto=texto, qtd_troca=troca):
    criptografia = ""
    for letra in plan_texto:
        posicao = alfabeto.index(letra)
        nova_posicao = posicao - qtd_troca
        criptografia += nova_posicao
        print(f"Seu descriptografia é {criptografia}")


if texto_usuario == "encode":
    encrypt(plan_texto=texto, qtd_troca=troca)
elif texto_usuario == "decode":
    decrypt(plan_texto=texto, qtd_troca=troca)
else:
    print("função não encontrada.")
    texto_usuario