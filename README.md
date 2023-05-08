# socketsClienteServidor
Programa de sockets de redes cliente e servidor

O programa de socket de rede socketCliente.py é um programa de geração e envio de mensagens de inteiros convertidos em strings, cujo número são de até 30 casas ou algarísmo e
são gerados aleatoriamente e automaticamente a cada 10 segundos. A mensagem com o núemro gerado é enviada para o servidor onde passa por um tratamento para identificar se
o número possui mais ou menos de 10 casas e caso possua menos de 10 casas ou algarísmos o tratamento realizado é para identificar se o número é ímpar ou par em seguida é retornada
uma mensagem ao cliente identificando o número caso este seja maior que 10 casas, e/ou identificando se este é par ou ímpar caso seja número menor de casas. A contagem de tempo de 10 segundos
é possível graças ao uso da biblioteca time. 
O programa de socket de rede socketCliente.py usa a biblioteca random para realizar a geração de números aleatórios. 
O programa de socket de rede socketCliente.py se conecta ao servidor através da porta 8888 e possue endereço de Host 127.0.0.1.

O programa de socket de rede socketServidor.py é um programa que mostra a mensagem de números aleatórios de até 30 casas gerados e enviados pelo programa de socket de
rede socketCliente.py. O programa inicia aguardando conexões de até no máximo 5 conexões simultâneas comom fora estabelecido no código do programa. Quando se conecta a 
um cliente o servidor informa com qual cliente está com conexão estabelecida. O programa socketServidor.py ele realiza o tratamento da mensagem recebida analisando a mensagem
e se na mensagem o número possuir mais de 10 casas ele envia o número que foi enviado em formato de mensagem de string e finaliza o tratamento e o programa pelos 10 segundos,
caso o número possua menos de 10 casas o programa faz o tratamento se o número é par ou ímpar e enviar a informação para o cliente que exibe essa informação e em seguida encerra
o tratamento e o programa por 10 segundos. O programa socketServidor.py se conecta através da porta 8888 e possui endereço de Host 127.0.0.1.
