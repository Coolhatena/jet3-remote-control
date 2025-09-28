import socket

# Printer ip address and port
ip = "192.168.0.110"
port = 3000

# Command data (Could be a single command or a command block)
action_command = "^0!NO" + chr(0x0D) # Edit the command sent to the printer here, keep the "+ chr(0x0D)" after the command 


# Connect with printer
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip, port))

# Send command data to printer
sock.send(action_command.encode())

sock.close()
