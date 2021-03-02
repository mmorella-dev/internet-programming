import logging

from simple_server import server
from polynomials import polynomials

logging.basicConfig(level=logging.INFO)

SERVER_PORT = 12345

# Define message handler command


def handle_command(client_msg: str):
    """
    Parse command as input to the functions in the polynomial library
    :param a client input string e.g 'E1.0 3.0 1.0'
    :returns an API response message e.g 'XInvalid input'
    """
    if len(client_msg) == 0:
        return 'X' + 'Client message was empty'
    # Parse string message
    command = client_msg[0]     # first character is an instruction
    params = client_msg[1:].split(" ")
    # Attempt to parse the input
    for i in range(0, len(params)):
        try:
            params[i] = float(params[i])
        except ValueError:
            return 'X' + f"could not convert string to float: '{params[i]}'"
    # Check that the command is valid
    if (command not in ('E', 'S')):
        return 'X' + f"Incorrect command type"
    # Verify the number of parameters
    if ((command == 'E' and len(params) < 2) or (command == 'S' and len(params) < 4)):
        return 'X' + 'Too few arguments'
    # Execute commands
    if (command == 'E'):
        logging.debug(
            f"Calling polynomials.evaluate({params[0]}, {params[1:]})")
        result = polynomials.evaluate(params[0], params[1:])
    elif (command == 'S'):
        if (params[-1] <= 0):
            return 'X' + f"Invalid tolerance"
        logging.debug(
            f"Calling polynomials.bisection({params[0]}, {params[1]}, {params[2:-1]}, {params[-1]})")
        result = polynomials.bisection(
            params[0], params[1], params[2:-1], params[-1])
    return command + str(result)


with server.create_listener(SERVER_PORT) as listener:
    # Loop until program is killed
    while True:
        server.accept_client(listener, handle_command)
