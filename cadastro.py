import json
import os

ARQUIVO = "cadastros.json"


def carregar_cadastros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_cadastros(cadastros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\nMenu:")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Excluir pessoa")
    print("4 - Sair")


def cadastrar_pessoa(cadastros):
    nome = input("Digite o nome: ")

    while True:
        idade = input("Digite a idade: ")
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("Idade inválida. Digite apenas números.")

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    cadastros.append(pessoa)
    salvar_cadastros(cadastros)
    print("Pessoa cadastrada com sucesso!")


def listar_pessoas(cadastros):
    if len(cadastros) == 0:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\nPessoas cadastradas:")
        for i, pessoa in enumerate(cadastros, start=1):
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']}")


def excluir_pessoa(cadastros):
    if len(cadastros) == 0:
        print("Não há cadastros para excluir.")
        return

    listar_pessoas(cadastros)

    while True:
        escolha = input("Digite o número da pessoa que deseja excluir: ")
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(cadastros):
                removida = cadastros.pop(indice)
                salvar_cadastros(cadastros)
                print(f"{removida['nome']} foi removida com sucesso.")
                break
            else:
                print("Número inválido.")
        else:
            print("Digite apenas números.")


def confirmar_saida():
    sair = input("Tem certeza que deseja sair? (s/n): ").lower()
    return sair == "s"


def main():
    cadastros = carregar_cadastros()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_pessoa(cadastros)

        elif opcao == "2":
            listar_pessoas(cadastros)

        elif opcao == "3":
            excluir_pessoa(cadastros)

        elif opcao == "4":
            if confirmar_saida():
                print("Encerrando o programa.")
                break

        else:
            print("Opção inválida. Tente novamente.")


main()