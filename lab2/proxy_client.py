import socket

BYTES_TO_READ = 4096


def get(host, port):
    # must have 2  newlines
    # requests need to be formatted for google.com
    request = b"GET / HTTP/1.1\nHOST: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        # shuts down the write part only so server can still send us a response
        s.shutdown(socket.SHUT_WR)
        print("Waiting for response!")
        chunk = s.recv(BYTES_TO_READ)
        result = b'' + chunk
        while (len(chunk) > 0):
            # print(chunk)
            chunk = s.recv(BYTES_TO_READ)
            result += chunk
        return result


print(get('127.0.0.1', 8080))
