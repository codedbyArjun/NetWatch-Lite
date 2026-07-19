# scanner/port_listener.py

import socket

PORT_SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NETBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT"
}

def scan_listening_ports():
    print("\n[+] NetWatch-Lite — Listening Port Scan\n")
    print("{:<10} {:<15} {:<10}".format("PORT", "SERVICE", "STATUS"))
    print("-" * 35)

    ip_address = input("Enter your IP address to scan (or press Enter to use localhost): ") or "127.0.0.1"

    for port, service in PORT_SERVICE_MAP.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip_address, port))

        if result == 0:
            print("{:<10} {:<15} {:<10}".format(port, service, "OPEN"))

        sock.close()

if __name__ == "__main__":
    scan_listening_ports()