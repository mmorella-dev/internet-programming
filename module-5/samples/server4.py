from reader_writer import reader_writer
import socket
import mimetypes
from server1 import send_string_response
from server2 import send_file_response
from os.path import join
import re

def read_line(rw):
    """
    reads and returns one line from the rw
    Line endings could be \n or \r\n
    :param rw: reader_writer object
    :return: one line
    """
    the_line=""
    ch=rw.read()
    while ch!='\r' and ch!='\n':
        the_line+=ch
        ch=rw.read()
    ch=rw.read()
    if ch!='\n' and ch!='\r':
        rw.unread(ch)
    return the_line


if __name__ == "__main__":
    listener=socket.socket()
    listener.bind(("",8080))
    listener.listen(0)

    while True:
        (sock, addr)=listener.accept()
        rw=reader_writer(sock)
        # read and parse all the contents of the request header
        first_line=read_line(rw)
        #print(first_line)
        first_line_parts=re.split(" +", first_line)
        #print(first_line_parts)
        #send_string_response(rw, "Hello")

        path=first_line_parts[1][1:]
        print(path)
        filepath=join('docs', path)
        print('filepath:', filepath)
        with open(filepath, 'rb') as file:
            data=file.read()
        mtype=mimetypes.guess_type(filepath)
        print(mtype)
        send_file_response(rw, data, content_type=mtype)





    sock.close()

















