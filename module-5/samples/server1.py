from reader_writer import reader_writer
import socket

def send_string_response(rw, message, content_type='text/plain', status = 200, status_remark='OK'):
    # first line    (HTTP/1.1, status_code, status_remark)
    rw.write("HTTP/1.1 {} {}".format(status, status_remark))
    # header
        # content-type, content-length
    rw.write("content-type: {}\n".format(content_type))
    rw.write("content-length: {}\n".format(rw.encoded_length(message)))
    # blank line
    rw.write("\n");
    # message body
    rw.write(message)


if __name__== "__main__":
    listener=socket.socket()
    listener.bind(("", 8080))
    listener.listen(0)

    while True:
        (sock, addr)=listener.accept()
        rw=reader_writer(sock)
        send_string_response(rw, "<h1>Hello there!</h1>")

    sock.close()

















