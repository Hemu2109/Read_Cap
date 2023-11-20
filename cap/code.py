from scapy.all import *
packet = rdpcap("dns.cap")
print(packet.show())