import http.server
import socketserver
import sys

PORT = 8000
DIRECTORY = "frontend"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server(port):
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving at http://localhost:{port}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Error: Port {port} is already in use.")
            print("Try using a different port or kill the process using this port.")
            print("To kill the process, run: lsof -i :{port} | grep LISTEN | awk '{print $2}' | xargs kill -9")
            sys.exit(1)
        else:
            raise
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
        sys.exit(0)

if __name__ == "__main__":
    run_server(PORT) 