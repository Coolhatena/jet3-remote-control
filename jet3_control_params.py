import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description="Send commands to a JET 3 printer via TCP/IP")
    parser.add_argument("--ip", required=True, help="Printer IP address")
    parser.add_argument("--port", type=int, required=True, help="Printer TCP port")
    parser.add_argument("--command", required=True, help="Command received by the printer")

    args = parser.parse_args()

    # STX (ASCII 2) y ETX (ASCII 3)
    stx = chr(2)
    etx = chr(3)

    mensaje = f"{stx}{args.command}{etx}\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((args.ip, args.port))
        sock.send(mensaje.encode())
        print(f"[OK] Comando enviado a {args.ip}:{args.port} -> <STX>{args.command}<ETX>")
    except Exception as e:
        print(f"[ERROR] No se pudo enviar: {e}")
    finally:
        sock.close()

    input("Presione Enter para salir...")

if __name__ == "__main__":
    main()
