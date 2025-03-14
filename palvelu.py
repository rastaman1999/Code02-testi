from wsgiref.simple_server import make_server

def app(environ, respond):
    respond('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "Morjesta w€rld😞!".encode('utf-8')
    yield "<form method=GET><input type=button value=paina></form>".encode("utf-8")

if __name__ == '__main__':
	with make_server("localhost", 8000, app) as server: 
            server.serve_forever()
