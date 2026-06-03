lista_planos = []

def criar_plano(id_plano, nome, valor_mensal, beneficios, descricao):
    novo_plano = {
        'id_plano': id_plano,
        'nome': nome,
        'valor_mensal': valor_mensal,
        'beneficios': beneficios,
        'descricao': descricao
    }
    lista_planos.append(novo_plano)
    print(f"Plano {nome} criado com sucesso!")

def listar_planos():
    if not lista_planos:
        print("Nenhum plano cadastrado")
        return
    for plano in lista_planos:
        print(f"ID: {plano['id_plano']}, Nome: {plano['nome']}, Valor Mensal: R${plano['valor_mensal']}, Beneficios: {plano['beneficios']}, Descrição: {plano['descricao']}")

def editar_plano(id_editar):
    for plano in lista_planos:
        if plano['id_plano'] == id_editar:
            print(f"Plano encontrado: {plano['nome']}")
            novo_nome = input("Digite o novo nome do plano (ou aperte ENTER para manter o atual): ")
            novo_valor = float(input("Digite o novo valor mensal do plano (ou aperte ENTER para manter o atual): "))
            novo_beneficios = input("Digite os novos beneficios do plano (ou aperte ENTER para manter o atual): ")
            nova_descricao = input("Digite a nova descrição do plano (ou aperte ENTER para manter o atual): ")

        if novo_nome != "":
            plano['nome'] = novo_nome
        if novo_valor != 0:
            plano['valor_mensal'] = novo_valor
        if novo_beneficios != "":
            plano['beneficios'] = novo_beneficios
        if nova_descricao != "":
            plano['descricao'] = nova_descricao

            print(f"Plano {plano['nome']} editado com sucesso!")
            return

def excluir_plano(id_excluir):
    for plano in lista_planos:
        if plano['id_plano'] == id_excluir:
            lista_planos.remove(plano)
            print(f"Plano {plano['nome']} excluído com sucesso.")
            return
        print("Plano não encontrado.")
    
