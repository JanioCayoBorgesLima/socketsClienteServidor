import socket
import random
import time

# Define o endereço IP e a porta para conexão
HOST = '127.0.0.1'
PORT = 8888

while True:
    # Cria um socket de cliente e se conecta ao servidor
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))

    # Gera um número inteiro aleatório com até 30 casas
    numero = random.randint(1, 9.99*(10**29))

    # Envia o número para o servidor
    cliente.send(str(numero).encode())

    # Recebe e imprime a mensagem do servidor
    mensagem = cliente.recv(1024).decode()
    print('Valor recebido do servidor:', mensagem + ' FIM')

    # Fecha a conexão com o servidor
    cliente.close()

    # Espera 10 segundos antes de se conectar novamente
    time.sleep(10)
