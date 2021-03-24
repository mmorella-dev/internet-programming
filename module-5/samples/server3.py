from reader_writer import reader_writer
import socket
import mimetypes
from server1 import send_string_response
from server2 import send_file_response

def read_line(rw):
    """
    reads and returns one line from the rw
    line endings could be \n or \r\n
    :param rw: reader_writer objedt
    :return: inintial line
    """
    first_line=""
    ch=rw.read()
    while ch!='\n' and ch!='\r':
        first_line+=ch
        ch=rw.read()
    return first_line


if __name__== "__main__":
    listener=socket.socket()
    listener.bind(("", 8080))
    listener.listen(0)

    while True:
        (sock, addr)=listener.accept()
        rw=reader_writer(sock)
        first_line=read_line(rw)
        print(first_line)
        send_string_response(rw, "Hello there!")

        # ? x=a & y=b
        # parsed_list=[?, x=a, &, y=b]

        # read and parse all the contents of the request header
        # declare one variable to make a HTML table
        # send the table back to client
        # then, you can check the result on your browser.


    sock.close()

















