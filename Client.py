import socket

def start_client(host='127.0.0.1', port=65432):
    """Start a simple TCP client."""
    # Initialize the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        # Send a message to the server
        message = "Hello, this is Bafin!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")
        
        # Receive a response from the server
        response = client_socket.recv(1024)
        print(f"Received: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print("Client shut down.")

if __name__ == "__main__":
    start_client()
