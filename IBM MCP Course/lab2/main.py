import os
import time
import socket
import asyncio
from dotenv import load_dotenv
from fastmcp import FastMCP, Client

def make_dir():
    if os.path.exists("path"):
        print("PAth directory already exists")
    else:
        print("✗ Path directory doesn't exist - creating it...")
        os.makedirs("path")
        print("✓ Path directory created")

PORT = 8000

def test_port(port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return True
        except socket.error:
            return False

print(f"Port {PORT} is available: {test_port()}")

def print_stream_info(read, write, _sid, verbose=False):
    """Print information about the read/write streams and session ID"""

    if verbose:
        print("READ (receives FROM server):")
        print(read)
        print()
        
        print("WRITE (sends TO server):")
        print(write)
        print()
        
        print("SESSION ID:")
        print(_sid())