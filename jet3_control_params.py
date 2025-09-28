import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description="Send commands to a JET 3 printer via TCP/IP")
    parser.add_argument("--ip", required=True, help="Printer IP address")
    parser.add_argument("--port", type=int, required=True, help="Printer TCP port")
    parser.add_argument("--command", required=True, help="Command received by the printer")

    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((args.ip, args.port))
    sock.send(args.command.encode())
    sock.close()

if __name__ == "__main__":
    main()
