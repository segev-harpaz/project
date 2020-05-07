from scapy.all import *


def http_header(packet):
    http_packet = str(packet)
    if http_packet.find('POST /result HTTP/1.1'):
        return True


t = sniff(count=1, prn=http_header, filter='tcp port 80')
print(t[0].show())
