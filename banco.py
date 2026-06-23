# credenciais do usuário para validação:
nome = 'Leonardo'
senha = '123'

#Funções
def consultaCategorias():
            lista = []
            with open("categorias.csv") as f:
                lista = [linha for linha in f.read().splitlines() if linha.strip()]
            n = 0
            print("\n")
            for linha in lista:
                colunas = linha.split(";")
                print("---------------")
                print("Categoria:",colunas[0])
                print("Valor -> R$:",colunas[1])
            print("\n")

            print("1-Sair")
            print("2-Adicionar Categoria")
            print("3-Editar Categoria")
            escolha2 = input("Escolha o que fazer: ")
            print("\n")
            
            if escolha2 == '2':

                print("Adicionar nova categoria")
                nome = input("Informe a categoria: ")
                valor = input("Informe o valor: ")
                with open("categorias.csv","a") as f:
                    f.write("\n")
                    f.write(nome)
                    f.write(";")
                    f.write(valor)
                    f.write(";")
                print("categoria adicinada.")
                print("\n")

            if escolha2 == '3':

                lista = []
                with open("categorias.csv") as f:
                    lista = [linha for linha in f.read().splitlines() if linha.strip()]
                n = 0
                nome = input("Qual categoria deseja modificar?: ")
                for linha in lista:
                    colunas = linha.split(";")
                    
                    if nome == colunas[0]:
                        print("Categoria:",colunas[0])
                        print("Valor -> R$:",colunas[1])
                        print("---------")
                        nome = input("Informe o novo nome: ")
                        valor = input("Informe o novo valor: ")
                        nova_categoria = nome + ";" + valor
                        lista[n] = nova_categoria
                        with open("categorias.csv","w") as f:
                            f.write("\n".join(lista))
                        print("Categoria salva com sucesso.")
                        break
                    n = n + 1
                else:
                    print("A data não foi encontrada.")

            else:

                return
def consultaEntradas():
        print("Entradas: ")
        lista = []
        with open("entradas.csv") as f:
                lista = [linha for linha in f.read().splitlines() if linha.strip()]
        n = 0
        print("\n")
        for linha in lista:
            colunas = linha.split(";")
            print("---------------")
            print("Data:",colunas[0])
            print("Valor -> R$:",colunas[1])
        print("\n")

        print("1-Sair")
        print("2-Adicionar Entrada")
        print("3-Editar Entrada")
        escolha3 = input("Escolha o que fazer: ")
        print("\n")
            
        if escolha3 == '2':
            print("Adicionar nova entrada")
            data = input("Informe a data: ")
            valor = input("Informe o valor: ")
            with open("entradas.csv","a") as f:
                f.write("\n")
                f.write(data)
                f.write(";")
                f.write(valor)
                f.write(";")
            print("entrada adicinada.")
            print("\n")

        if escolha3 == '3':

            lista = []
            with open("entradas.csv") as f:
                lista = [linha for linha in f.read().splitlines() if linha.strip()]
            n = 0
            nome = input("Qual entrada deseja modificar?: ")
            for linha in lista:
                colunas = linha.split(";")
                
                if nome == colunas[0]:
                    print("Entrada:",colunas[0])
                    print("Valor -> R$:",colunas[1])
                    print("---------")
                    data = input("Informe a nova data: ")
                    valor = input("Informe o novo valor: ")
                    nova_entrada = data + ";" + valor
                    lista[n] = nova_entrada
                    with open("entradas.csv","w") as f:
                        f.write("\n".join(lista))
                    print("Entrada salva com sucesso.")
                    break
                n = n + 1
            else:
                print("A entrada não foi encontrada.")

def consultaSaidas():
        print("Saídas: ")
        lista = []
        with open("saidas.csv") as f:
                lista = [linha for linha in f.read().splitlines() if linha.strip()]
        n = 0
        print("\n")
        for linha in lista:
            colunas = linha.split(";")
            print("---------------")
            print("Data:",colunas[0])
            print("Valor -> R$:",colunas[1])
        print("\n")

        print("1-Sair")
        print("2-Adicionar Saída")
        print("3-Editar Saída")
        escolha3 = input("Escolha o que fazer: ")
        print("\n")
            
        if escolha3 == '2':
            print("Adicionar nova saída")
            data = input("Informe a data: ")
            valor = input("Informe o valor: ")
            with open("saidas.csv","a") as f:
                f.write("\n")
                f.write(data)
                f.write(";")
                f.write(valor)
                f.write(";")
            print("saída adicionada.")
            print("\n")

        if escolha3 == '3':

            lista = []
            with open("saidas.csv") as f:
                lista = [linha for linha in f.read().splitlines() if linha.strip()]
            n = 0
            nome = input("Qual saída deseja modificar?: ")
            for linha in lista:
                colunas = linha.split(";")
                
                if nome == colunas[0]:
                    print("Saída:",colunas[0])
                    print("Valor -> R$:",colunas[1])
                    print("---------")
                    data = input("Informe a nova data: ")
                    valor = input("Informe o novo valor: ")
                    nova_saida = data + ";" + valor
                    lista[n] = nova_saida
                    with open("saidas.csv","w") as f:
                        f.write("\n".join(lista))
                    print("Saída salva com sucesso.")
                    break
                n = n + 1
            else:
                print("A saída não foi encontrada.")

def gerarRelatorio():
    print("Relatório do Mês:")
    lista = []
    with open("entradas.csv") as f:
            lista = [linha for linha in f.read().splitlines() if linha.strip()]

    total_entradas = 0
    for linha in lista:
        colunas = linha.split(";")
        total_entradas += float(colunas[1])

    print("Total de Entradas: R$", total_entradas)

    with open("saidas.csv") as f:
            lista = [linha for linha in f.read().splitlines() if linha.strip()]

    total_saidas = 0
    for linha in lista:
        colunas = linha.split(";")
        total_saidas += float(colunas[1])
    print("Total de Saídas: R$", total_saidas)



    saldo = total_entradas - total_saidas
    print("Saldo do mês(entradas-saidas): R$", saldo,"\n")
# Fim funções            
print("\033[32m\n---Bem vindo ao sistema de finanças" ,nome,"---\033[0m")
senhaVldc = input("Digite a sua senha: ")

if senhaVldc == senha:
    print("\033[01mAcesso Permitido\033[0m")

    print("\n")

    while True:
        print("1 - Consultas as categorias dos gastos")
        print("2 - Consultar as entradas")
        print("3 - Consultar as saídas")
        print("4 - Gerar um relatório")
        print("5 - Sair")
        escolha = input("Escolha o que fazer: ")
    
        if escolha == '5':
            print("\033[01mAté mais!\033[0m")
            break

        elif escolha == '1':
            
            consultaCategorias()

        elif escolha == '2':
            consultaEntradas()

        elif escolha == '3':
            consultaSaidas()

        elif escolha == '4':
            gerarRelatorio()

        else:
            print("Opção Inválida")
            break
    




