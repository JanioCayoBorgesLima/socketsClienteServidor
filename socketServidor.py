import socket

# Define o endereço IP e a porta para conexão
HOST = '127.0.0.1'
PORT = 8888

# Cria um socket de servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))

# Define o número máximo de conexões simultâneas
servidor.listen(5)

print('Servidor aguardando conexões...')

while True:
    # Espera a conexão de um cliente
    conexao, endereco = servidor.accept()
    print('Conexão estabelecida com', endereco)

    # Recebe o número do cliente
    numero = conexao.recv(1024)
    numero = int(numero.decode())

    # Verifica se o número tem mais de 10 casas
    if len(str(numero)) > 10:
        # Gera uma string do mesmo tamanho e envia para o cliente
        mensagem = str(numero)
        conexao.send(mensagem.encode())
    else:
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            mensagem = 'PAR'
        else:
            mensagem = 'ÍMPAR'
        conexao.send(mensagem.encode())

    # Fecha a conexão com o cliente
    conexao.close()
