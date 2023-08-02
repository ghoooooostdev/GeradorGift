import random
import string
import os
import datetime

def limpar_tela():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def gerar_codigo_psn():
    codigo_psn = ''.join(random.choices(string.digits, k=10))
    return codigo_psn

def gerar_codigo_google_play():
    codigo_google_play = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return codigo_google_play

def gerar_codigo_apple_store():
    codigo_apple_store = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return codigo_apple_store

def salvar_codigo(codigos, servico):
    nome_arquivo = input("Digite o nome do arquivo de saída: ")
    if not nome_arquivo.endswith(".txt"):
        nome_arquivo += ".txt"

    with open(nome_arquivo, "a") as arquivo:
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arquivo.write(f"{servico} - {data_hora}\n")
        for codigo in codigos:
            arquivo.write(f"Código: {codigo}\n")
        arquivo.write("-" * 30 + "\n")
    print(f"Códigos salvos com sucesso no arquivo '{nome_arquivo}'!")

def exibir_menu():
    print("\033[1;31mGerador de Gift Cards - @Ghoooooostdev\033[0m")
    print("Opções:")
    print("1. Google Play")
    print("2. Apple Store")
    print("3. PSN")
    print("4. Visualizar códigos gerados")
    print("5. Limpar códigos gerados")
    print("0. Sair")

def visualizar_codigos():
    try:
        with open("codigos_gerados.txt", "r") as arquivo:
            conteudo = arquivo.read()
            if conteudo:
                print("Códigos gerados anteriormente:\n")
                print(conteudo)
            else:
                print("Nenhum código gerado anteriormente.")
    except FileNotFoundError:
        print("Nenhum código gerado anteriormente. O arquivo 'codigos_gerados.txt' ainda não existe.")

def limpar_codigos():
    try:
        with open("codigos_gerados.txt", "w") as arquivo:
            arquivo.write("")
        print("Códigos gerados foram apagados com sucesso!")
    except FileNotFoundError:
        print("Nenhum código gerado anteriormente.")

def gerar_codigos_em_quantidade(opcao, quantidade):
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    
    codigos_gerados = []
    servico = ""
    gerador_codigo = None

    if opcao == 1:
        servico = "Google Play"
        gerador_codigo = gerar_codigo_google_play
    elif opcao == 2:
        servico = "Apple Store"
        gerador_codigo = gerar_codigo_apple_store
    elif opcao == 3:
        servico = "PSN"
        gerador_codigo = gerar_codigo_psn

    for _ in range(quantidade):
        codigo = gerador_codigo()
        codigos_gerados.append(codigo)

    return servico, codigos_gerados

def obter_opcao_menu():
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao in [0, 1, 2, 3, 4, 5]:
                return opcao
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")

def main():
    while True:
        limpar_tela()
        exibir_menu()
        opcao = obter_opcao_menu()

        if opcao == 0:
            print("Saindo do programa. Obrigado por usar o Gerador de Gift Cards!")
            break
        elif opcao == 1 or opcao == 2 or opcao == 3:
            quantidade = int(input("Digite a quantidade de códigos a serem gerados: "))
            servico, codigos_gerados = gerar_codigos_em_quantidade(opcao, quantidade)

            print(f"Códigos {servico} gerados:")
            for codigo in codigos_gerados:
                print(codigo)

            salvar = input("Deseja salvar os códigos gerados? (S/N): ")
            if salvar.lower() == "s":
                salvar_codigo(codigos_gerados, servico)
        elif opcao == 4:
            while True:
                limpar_tela()
                visualizar_codigos()
                escolha = input("\nPressione Enter para continuar, 'V' para voltar ao menu principal ou 'Q' para sair: ").lower()
                if escolha == "":
                    break
                elif escolha == "v":
                    break
                elif escolha == "q":
                    print("Saindo do programa. Obrigado por usar o Gerador de Gift Cards!")
                    exit()
                else:
                    print("Opção inválida! Por favor, escolha uma opção válida.")
        elif opcao == 5:
            limpar_codigos()

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
