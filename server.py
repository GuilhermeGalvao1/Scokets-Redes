import socket

IP_SERVIDOR = ''

PORTA = 8000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

conexao = (IP_SERVIDOR, PORTA)
udp.bind(conexao)

while 1:
    Mensagem, endereco = udp.recvfrom(1024)

    print("Mensagem do cliente:", Mensagem.decode())
    print("Endereço do cliente:", endereco)