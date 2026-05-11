senha = input("Digite uma senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

caracteres_especiais = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

for caractere in senha:

    if caractere.isupper():
        tem_maiuscula = True

    elif caractere.islower():
        tem_minuscula = True

    elif caractere.isdigit():
        tem_numero = True

    elif caractere in caracteres_especiais:
        tem_especial = True

requisitos_faltando = []

if len(senha) < 8:
    requisitos_faltando.append("Mínimo de 8 caracteres")

if not tem_maiuscula:
    requisitos_faltando.append("Uma letra maiúscula")

if not tem_minuscula:
    requisitos_faltando.append("Uma letra minúscula")

if not tem_numero:
    requisitos_faltando.append("Um número")

if not tem_especial:
    requisitos_faltando.append("Um caractere especial")

if len(requisitos_faltando) == 0:
    print("Senha forte!")
else:
    print("\nA senha não atende aos seguintes requisitos:")

    for requisito in requisitos_faltando:
        print("-", requisito)