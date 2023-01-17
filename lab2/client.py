import socket

BYTES_TO_READ = 4096  # small amounts are more reliable


def get(host, port):
    # must have 2  newlines
    request = b"GET / HTTP/1.1\nHost:" + host.encode("utf8") + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(request)
    # shuts down the write part only so server can still send us a response
    s.shutdown(socket.SHUT_WR)
    result = s.recv(BYTES_TO_READ)
    while (len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    s.close()


get('www.google.com', 80)
