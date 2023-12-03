import socketserver
import random

def index():
    print('----- index')
    return '''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/contact">Contact me</a> <br />
    '''

def about_me():
    print('----- about me')
    return '''
        <h1>About me</h1>
        <p>My name is Ash Ketchum</p>
        <p>I have a Pikachu</p>
    '''

def contact_me(path):
    print('---CONTACT ME')
    print(path)
    print('---')
    return '''
        <h1>Contact</h1>
        <form method="GET" action="/contact">
            <input name="myname" placeholder="Your name" />
            <button>Submit</button>
        </form>
    '''

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        # Every time a request comes in, it calls this method

        ## Step 1, parse the request data
        # Get the top line of the request
        top_line = self.rfile.readline().decode('ascii')
        method, path, http_version = top_line.split(' ', 2)
        print('--> Receiving %s request for %s' % (method, path))

        # Get the HTML value associated with the path that is getting requested
        # from the pages dictionary
        if path == '/':
            body = index()
        elif path == '/about-me':
            body = about_me()
        elif path.startswith('/contact'):
            body = contact_me(path)
        else:
            # Couldn't find page, send back 404 error page, and be sure to set
            # the 404 status code in the header
            body = '<h1>Oh no, 404! Jigglypuff prolly stole it.</h1>'

        # Write the response headers text/html 
        self.wfile.write(b'HTTP/1.0 200 OK\n')
        self.wfile.write(b'Content-Type: text/html\n')

        # The HTTP standard mandates an extra return character here, separating
        # the headers from the body of the response.
        self.wfile.write(b'\n')
        self.wfile.write(bytes(body, 'ascii'))
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

