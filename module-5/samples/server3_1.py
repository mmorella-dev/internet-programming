from reader_writer import reader_writer
import socket
import mimetypes
from server1 import send_string_response
from server2 import send_file_response
import re


html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
"""

html_end="""
</body>
</html>
"""




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

        header_line=read_line(rw)
        #print(header_line)
        header_parts=re.split(": ", header_line)
        #print(header_parts)
        headers={}
        headers[header_parts[0]]=header_parts[1]
        #headers['Host']= localhost
        #print(headers)

        header_line=read_line(rw)
        while header_line:
            header_parts=re.split(': ', header_line)
            headers[header_parts[0]] = header_parts[1]
            header_line = read_line(rw)
        print(headers)

        # code to creat html table with the headers
        html+="<p>method:{}</p>".format(first_line_parts[0])
        html+="<table>"
        for k in headers:
            html+="<tr><td>{}</td><td>{}</td></tr>".format(k, headers[k])
        html+="</table>"
        html=html+html_end
        send_string_response(rw, html)

        # ? x=a & y=b
        # parsed_list=[?, x=a, &, y=b]

        # read and parse all the contents of the request header
        # declare one variable to make a HTML table
        # send the table back to client
        # then, you can check the result on your browser.


    sock.close()

















