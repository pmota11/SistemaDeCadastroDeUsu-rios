usu = []

def l_usu():
    if not usu:
        print("não existem usuários cadastrados")
    else:
        print("usuários cadastrados:")
        for usuario in usu:
            print(f" - {usuario[0]}")

def cd_usu():
    nome = input("digite o nome do usuário: ")
    email = input("digite o email do usuário: ")
    senha = input("digite a senha do usuário: ")
    acesso = input("digite o nível de acesso do usuário (1 - administrador / 2 - convidado): ")
    cpf = input("digite o cpf do usuário: ")

    if acesso not in ['1', '2']:
        print("nível de acesso inválido")
        return
    
    usuario = (nome, email, senha, acesso, cpf)
    usu.append(usuario)

def logar(): 
    cpf = input("digite o cpf para login: ")

    usu_encontrado = None
    for usuario in usu:
        if usuario[4] == cpf:
            usu_encontrado = usuario
            break

    if usu_encontrado:
        senha = input("digite sua senha: ")
        if usu_encontrado[2] == senha:
            print("Logado")
            return usu_encontrado

        else:
            print("senha invalida")

    else:
        print("usuário não encontrado")
    
    return None

def edit_usu(cpf_logado):

    if cpf_logado is None or cpf_logado[3] != '1':
        print("apenas administradores podem editar usuários")
        return
    
    cpf = input("digite o CPF do usuário que deve ser editado")
    
    usu_encontrado = None
    for usuario in usu:
        if usuario[4] == cpf:
            usu_encontrado = usuario
            break

    if usu_encontrado:
        nome = input("digite o novo nome para o usuário")
        email = input("digite o novo email ao usuário")
        senha = input("digite uma nova senha ao usuário")
        acesso = input("digite o novo nível de acesso do usuário")

        novo_usu = (
            nome if nome else usu_encontrado[0],
            email if email else usu_encontrado[1],
            senha if senha else usu_encontrado[2],
            acesso if acesso else usu_encontrado[3],
            usu_encontrado[4]
        )
    
        usu[usu.index(usu_encontrado)] = novo_usu
        print("usuário editado")

    else:
        print("usuário não encontrado")

def p_usu(cpf_logado):
    
    if cpf_logado is None:
        print("você precisa estar logado para procurar um usuário")
        return

    cpf = input("digite o cpf do usuário a ser procurado: ")

    usu_encontrado = None
    for usuario in usu:
        if usuario[4] == cpf:
            usu_encontrado = usuario
            break

    if usu_encontrado:
        if cpf_logado and cpf_logado[3] == '1':
            print(f"Nome: {usu_encontrado[0]}")
            print(f"E-mail: {usu_encontrado[1]}")
            print(f"Senha: {usu_encontrado[2]}")
            print(f"Nível de Acesso: {usu_encontrado[3]}")
            print(f"CPF: {usu_encontrado[4]}")

        else: 
            print(f"Nome: {usu_encontrado[0]}")

    else:
        print("usuario nao encontrado")

def sair():
    print("encerrando sistema")

def sistema():
    usu_log =None


    while True:
        print("Selecione a opção desejada:" \
"\n1- Listar Usuários" \
"\n2- Cadastrar Usuários" \
"\n3- Logar Usuário" \
"\n4- Editar Usuário por CPF" \
"\n5- Procurar Usuário por CPF" \
"\n6- SAIR")

        try:
            op = int(input("Digite a opção: "))

            if op == 6:
                sair()
                break

            elif op == 1:
                l_usu()

            elif op == 2:
                cd_usu()

            elif op == 3:
                usu_log = logar()

            elif op == 4:
                if usu_log is not None:  
                    edit_usu(usu_log)
                else:
                    print("você precisa estar logado para editar um usuário")

            elif op == 5:
                if usu_log is not None:  
                    p_usu(usu_log)
                else:
                    print("você precisa estar logado para procurar um usuário")
        except:
            print("opção selecionada, invalida")

sistema()