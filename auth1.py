# Felipe Fernandes Bortolino
# Nicolas Aparecido Ferreira
import hashlib

def salvar_arquivo(nome_arquivo, nome_usuario, senha):
    with open(nome_arquivo, 'a+') as arquivo:
        hash_senha = hashlib.sha256(senha.encode())
        hash_senha = hash_senha.hexdigest()
        arquivo.write(f"{nome_usuario},{hash_senha}\n")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        usuarios = []
        for linha in linhas:
            usuario, senha = linha.strip().split(",")
            usuarios.append((usuario, senha))

    return usuarios

ARQUIVO = 'usuarios.txt'
usuario1 = input("Digite seu usuário: ")
senha1 = input("Digite sua senha: ")

# Identificação do usuário
usuarios = ler_arquivo(ARQUIVO)
salvar_arquivo(ARQUIVO, usuario1, senha1)

nome_usuario = input("Digite seu usuário: ")
senha_usuario = input("Digite sua senha: ")
 
for usuario in usuarios:
    nome = usuario[0]
    senha = usuario[1]

    # SUBSTITUIR POR CÓDIGO
    # Verifico nome de usuário e, se existir, mostro que o usuário existe e paro execução do loop (break)
    # Senão, mostro que o usuário não existe e paro execução do loop (break)
    if nome == nome_usuario:
        print("Usuário existente")
    else:
     print("Usuário não encontrado")
     break
    # FIM SUBSTITUIR POR CÓDIGO

# Autenticação
for usuario in usuarios:
    nome = usuario[0]
    senha = usuario[1]

    # SUBSTITUIR POR CÓDIGO
    # Verifico nome de usuário e, se existir, faço autenticação comparando senha fornecida pelo teclado
    # com senha armazenada na variável 'senha'.
    #   Se as senhas forem iguais, então mostre para o usuário "Seja bem vindo" e pare a execução do loop (break)  
    #   Senão, mostre "Usuário ou senha incorreto" e pare a execução do loop (break)  
    # FIM SUBSTITUIR POR CÓDIGO
  