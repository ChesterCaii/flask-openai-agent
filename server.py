"""
Frontend Server Module

This module provides a simple HTTP server to serve the frontend files.
It's used during development to avoid CORS issues.
"""

import http.server
import socketserver
import sys
from config import FRONTEND_PORT

class Handler(http.server.SimpleHTTPRequestHandler):
    """Handler for serving frontend files."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="frontend", **kwargs)

def run_server(port):
    """
    Run the frontend server on the specified port.
    
    Args:
        port (int): The port to run the server on
        
    Raises:
        OSError: If the port is already in use
        KeyboardInterrupt: If the server is stopped with Ctrl+C
    """
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving frontend at http://localhost:{port}")
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
    run_server(FRONTEND_PORT) 