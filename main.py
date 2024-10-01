import hashlib

#A-----------------------------------------------
mensagem = input("Digite sua mensagem: ")
hash1 = hashlib.md5(mensagem.encode())

mensagem_final = mensagem + "." + hash1.hexdigest()
print(f"{mensagem_final}")
#B-----------------------------------------------
mensagem_recebida = mensagem_final.split(".")[0]
codigo_recebido = mensagem_final.split(".")[1]

#Verifica a mensagem-----------------------------
hash2 = hashlib.md5(mensagem.encode())
hash2 = hash2.hexdigest()

#Compara se o código recebido é o mesmo que foi enviado
if hash2 == hash1.hexdigest():
    print("A mensagem não foi alterada!")
else:
    print("A MENSAGEM FOI ALTERADA, NÃO CONFIE NA MENSAGEM!")