# main.py

from Scanner.port_listener import scan_listening_ports

def main():
    print("[*] Starting NetWatch-Lite...\n")
    scan_listening_ports()

if __name__ == "__main__":
    main()