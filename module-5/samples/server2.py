from reader_writer import reader_writer
import socket
import mimetypes


def send_file_response(rw, message, content_type='text/plain', status = 200, status_remark='OK'):
    # first line    (HTTP/1.1, status_code, status_remark)
    rw.write("HTTP/1.1 {} {}".format(status, status_remark))
    # header
        # content-type, content-length
    rw.write("content-type: {}\n".format(content_type))
    rw.write("content-length: {}\n".format(len(message)))
    # blank line
    rw.write("\n")
    # message body
    rw.socket.sendall(message)


if __name__== "__main__":
    listener=socket.socket()
    listener.bind(("", 8080))
    listener.listen(0)

    while True:
        (sock, addr)=listener.accept()
        rw=reader_writer(sock)
        filename="event.html"
        with open(filename, 'rb') as file:
            data=file.read()
        mtype=mimetypes.guess_type(filename)
        print(mtype)
        send_file_response(rw, data, content_type=mtype)

    sock.close()

















