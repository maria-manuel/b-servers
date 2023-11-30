import socketserver

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Every time a TCP connection is opened, it calls this method

        # The request data is in a file-like object called 'self.rfile' that we
        # can read. We need to "decode" it since it comes in as bytes.
        print('---- REQUEST -------------')
        request = self.rfile.readline().decode('ascii').strip()
        print(request)
        print('--------------------------')

        # (Bonus Challenge code goes here)

        # Just say the same thing to all requests, the 200 OK reply required by
        # the HTTP protocol, then the text "Hello server world!"
        self.wfile.write(b'HTTP/1.1 200 OK\n\n')
        self.wfile.write(b'Welcome to my homepage!')

        # Close off the connection ("hang up")
        self.wfile.close()


###################################################################
# NOTE: The rest of this file is some dense boilerplate that's not useful for
# your learning to understand.
if __name__ == "__main__":
    PORT = 8080
    server = None
    try:
        socketserver.TCPServer.allow_reuse_address = True
        server = socketserver.TCPServer(('', PORT), RequestHandler)
        print('--------> Starting server on port ', PORT)
        server.serve_forever()

    finally:
        print('\n-------> Shutting down the web server')
        if server:
            server.server_close()

