import socket

target = input("Masukkan IP atau domain target: ")
port_range = range(1, 100)  # port 1-99

print(f"\nMemindai port terbuka pada {target}...\n")
for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} terbuka")
    sock.close()
