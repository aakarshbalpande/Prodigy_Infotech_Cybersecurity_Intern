from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto
        
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"TCP Payload: {bytes(tcp_layer.payload)}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"UDP Payload: {bytes(udp_layer.payload)}")
        elif Raw in packet:
            raw_layer = packet[Raw]
            print(f"Raw Payload: {bytes(raw_layer)}")

def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()