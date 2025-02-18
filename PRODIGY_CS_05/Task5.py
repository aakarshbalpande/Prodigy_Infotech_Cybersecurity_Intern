from scapy.all import sniff, get_if_list

def packet_callback(packet):
    print(packet.summary())
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"Payload: {payload}")
        print("-" * 50)
def start_sniffing(interface):
    print(f"Starting packet sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)
if __name__ == "__main__":
    print("Available network interfaces:")
    print(get_if_list())
    interface = "Wi-Fi"  
    start_sniffing(interface)