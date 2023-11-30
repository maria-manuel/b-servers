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

        # (Bonus Challenge code goes here) = pseudocode of what happens

        # If the request is only "/"
        #    then, reply with homepage
        if request == "GET / HTTP/1.1":
            self.wfile.write(b'HTTP/1.1 200 OK\n \n')
            self.wfile.write(b'<h1>Welcome to my homepage!</h1>')
            self.wfile.write(b'<p><a href="/about-me>Learn more about me</a></p>')
            self.wfile.write(b'<p><a href="/contact-me">Send me an email</a></p>')
        # If the request contains like "/about-me"
        #    then reply with a about me page
        elif request == "GET /about-me HTTP/1.1":
            self.wfile.write(b'HTTP/1.1 200 OK\n \n')
            self.wfile.write(b'<h1>About me!</h1>')
            self.wfile.write(b'<p>I am a coder</p>')
        # If the request is something like "/contact me"
        #    Then reply with a contact page
        elif request == "GET /contact-me HTTP/1.1":
            self.wfile.write(b'HTTP/1.1 200 OK\n \n')
            self.wfile.write(b'<h1>Contact</h1>')
            self.wfile.write(b'<p>Wanna hear from you!</p>')

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

