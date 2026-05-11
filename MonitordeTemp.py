LIMITE_TEMPERATURA = 80

sistema_ligado = True

print("=== MONITOR DE TEMPERATURA ===")

while sistema_ligado:

    entrada = input(
        "\nDigite a temperatura do servidor "
        "(ou 'desligar' para encerrar): "
    )

    if entrada.lower() == "desligar":
        sistema_ligado = False
        print("Sistema de monitoramento encerrado.")
    
    else:
        temperatura = float(entrada)

        print(f"Temperatura atual: {temperatura} °C")

        if temperatura > LIMITE_TEMPERATURA:
            print("ALERTA: Resfriamento ativado!")
        else:
            print("Temperatura dentro do limite seguro.")
            