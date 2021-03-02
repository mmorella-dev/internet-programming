# polynomial_client.py

import socket
from time import sleep
import logging

SERVER_IP = "localhost"
SERVER_PORT = 12345


def create_connection(ip: str, port: int):
    sock = socket.socket()
    while True:
        try:
            sock.connect((ip, port))
            logging.info(f"Connected to {ip}:{port}")
            return sock
        except OSError as err:
            logging.error(err)
            logging.info(
                f"Failed while connecting to {ip}:{port}. Try again in 3 seconds...")
            sleep(3)


def send_message(sock: socket.socket, message: str):
    message_byte = message.encode()
    sock.sendall(message_byte)
    logging.info(f"Sent message: `{message}`")
    return sock


def receive_message(sock: socket.socket) -> str:
    msg: str = ""
    while True:
        bytes = sock.recv(2048)
        if len(bytes) == 0:
            break
        msg += bytes.decode()  # UTF-
    if (len(msg) > 0):
        logging.info(f"Received message: \"{msg}\"")
    return msg


def make_request(msg: str):
    with create_connection(SERVER_IP, SERVER_PORT) as sock:
        send_message(sock, msg)
        sock.shutdown(1)
        return receive_message(sock)


testing_strings = (["E1.0 -945 1689 -950 230 -25 1", "E0.0"],
                   ["S0 2 -945 1689 -950 230 -25 1 1e-15",
                    "S1.0000000000000004"],
                   ["G4.1 0 0", "XIncorrect command type"],
                   ["4 1 0",  "Xcould not convert string to float: ''"],
                   ["E1.0", "XToo few arguments"],
                   ["S1.0", "XToo few arguments"],
                   ["S0 2 -945 1689 -950 230 -25 1 -1e-15",
                    "XInvalid tolerance"],
                   ["Not a number",
                    "Xcould not convert string to float: 'ot'"],
                   ["S0 2 -945 1689 -950 230 -25 1 0",
                    "XInvalid tolerance"],
                   ["S0 2 -945 1689 -950 230 G 1 1e-15", "Xcould not convert string to float: 'G'"])

# logging.basicConfig(level=logging.INFO)

for input, expected in testing_strings:
    print(f"📤  Sent: `{input}`")
    response = make_request(input)
    print(f"📩  Recv: `{response}`")
    if (response != expected):
        print(f"❌  Expected: `{expected}`")
    else:
        print(f"✅  Matched expected response")
    print("")
