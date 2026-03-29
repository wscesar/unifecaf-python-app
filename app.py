import math


tabela = {}


def cadastrar_peca():
    print("\n--- Cadastro Peça ---")
    id_peca = input("Digite o ID da peça: ").strip()
    
    if not id_peca:
        print("ID da peça não pode ser vazio.")
        return

    if id_peca in tabela:
        print(f"O ID '{id_peca}' já existe no sistema.")
        return

    try:
        cor = input("Digite a cor (azul ou verde): ").strip()
        peso = float(input("Digite o peso em gramas (min: 95 / max: 105): "))
        comprimento = float(input("Digite o comprimento em cm (min: 10 / max: 20):"))
    except ValueError:
        print("Valor inválido.")
        return

    validar(id_peca, peso, cor, comprimento)
    

def validar(id_peca, peso, cor, comprimento):
    motivos = []
    aprovada = False
    
    if peso < 95 or peso > 105:
        motivos.append("Peso fora do limite")
        
    if cor.strip().lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")
        
    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do limite")
    
    if len(motivos) == 0:
        aprovada = True
    
    if not aprovada:
        print("Reprovada")
    else:
        print("Aprovada")
    
    salvar_peca(id_peca, peso, cor, comprimento, aprovada, motivos)


def salvar_peca(id_peca, peso, cor, comprimento, aprovada, motivos):
    tabela[id_peca] = {
        "cor": cor,
        "peso": peso,
        "comprimento": comprimento,
        "aprovada": aprovada,
        "motivos": motivos
    }


def relatorio():
    print("\n--- Relatório ---")
    
    total_aprovadas = 0
    total_reprovadas = 0
    
    for peca in tabela.values():
        if peca["aprovada"]:
            total_aprovadas += 1
        else:
            total_reprovadas += 1
            
    print(f"Caixas utilizadas         : {math.ceil(total_aprovadas / 10)}")
    print(f"Total de Peças Aprovadas  : {total_aprovadas}")
    print(f"Total de Peças Reprovadas : {total_reprovadas}")
    
    if total_reprovadas > 0:
        print("\nMotivo das Reprovações:")
        
        for id_peca, dados in tabela.items():
            if dados["aprovada"] == False:
                print(f"  - Peça {id_peca}: {', '.join(dados['motivos'])}")


def exibir_menu():
    print("\n---SISTEMA DE CONTROLE---")
    print("1. Cadastrar peça")
    print("2. Relatório")
    print("0. Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            relatorio()
        elif opcao == '0':
            print("Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
