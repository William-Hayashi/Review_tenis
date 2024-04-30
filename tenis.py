
def saudacoes():
    print("__________________________________")
    print("Seja Bem Vindo ao NossoReview!")
    print("Aqui você pode conferir os melhores reviews de tênis do mundo da corrida")
    print("__________________________________")


#LOGIN E LOGOUT

def inicio():
    
    print("Opção 1 - Adicionar um review de um tênis")
    print("Opção 2 - Visualizar um review de um tênis")
    print("Opção 3 - Editar um review de um tênis")
    print("Opção 4 - Excluir um review de um tênis")
    print("Opção 5 - Sair da plataforma")

    



def validacao():
    global resposta_user
    try:
        resposta_user = int(input("Escolha a opção que deseja: "))
        print("A opção escolhida foi a opção {}".format(resposta_user))
        if resposta_user == 1:
            adicionar()
            print("Processando...")
        elif resposta_user == 2:
            visualizar()
            print("Processando...")
        elif resposta_user == 3:
            editar()
            print("Processando...")
        elif resposta_user == 4:
            excluir()
            print("Processando...")
        else:
            print("O valor não está entre 1 e 4, por tanto não é válido")

    except ValueError:
       print("O valor digitado não é um número válido")

def adicionar():
    dict = {nome, modelo, marca, review}
    nome = input("Digite o nome do tênis")
    modelo = input("Digite o modelo do tênis")
    marca = input("Digite a marca do tênis")
    review = input("Digite o review do tênis")


    resposta_confimacao = input("Deseja confirmar o review? Sim ou Não").upper()
    if resposta_confimacao == 'SIM':
        print("Review salvo com sucesso!")
        return inicio()
    elif resposta_confimacao == "NÃO":
        resposta_alteracao = input("Deseja alterar o review atual? SIM ou NÃO").upper()
        if resposta_alteracao == 'SIM':
            review_editar = input("Qual categoria deseja mudar: (nome, modelo, marca, review)")
            novo_review = input("Digite a nova descrição: ")

            dict[review_editar] = novo_review
            print("Alterado com sucesso:")


def visualizar():

def editar():

def excluir():



            
        
    
