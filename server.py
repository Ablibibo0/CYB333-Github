import socket

def start_server(host='127.0.0.1', port=65432):
    """Start a simple TCP server."""
    # Initialize the socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Bind the socket to the specified host and port
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")
        
        # Listen for incoming connections
        server_socket.listen(1)
        print("Waiting for a connection...")
        
        while True:
            # Accept a connection from a client
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            try:
                # Receive data from the client
                data = conn.recv(1024)
                if data:
                    print(f"Received: {data.decode('utf-8')}")
                    # Send a response back to the client
                    conn.sendall(b"Hello from the server!")
            except Exception as e:
                print(f"Error during communication: {e}")
            finally:
                # Close the connection
                conn.close()
                print(f"Connection with {addr} closed.")
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        # Close the server socket
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    start_server()


