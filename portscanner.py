import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """
    Scans a single port on the target host.
    :param host: The target host (IP or hostname).
    :param port: The port number to scan.
    :return: None
    """
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the connection attempt
            s.settimeout(1)
            # Attempt to connect to the target host and port
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open on {host}")
            else:
                pass  # Port is closed; do nothing
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def validate_target(target):
    """
    Validates the target host to ensure it is localhost or scanme.nmap.org.
    :param target: The target host (IP or hostname).
    :return: True if valid, False otherwise.
    """
    allowed_targets = ["127.0.0.1", "localhost", "scanme.nmap.org"]
    return target in allowed_targets

def port_scanner(host, start_port, end_port, threads=10):
    """
    Scans a range of ports on the target host.
    :param host: The target host (IP or hostname).
    :param start_port: Starting port number.
    :param end_port: Ending port number.
    :param threads: Number of threads for concurrent scanning.
    :return: None
    """
    print(f"Scanning {host} from port {start_port} to {end_port}...")

    # Use ThreadPoolExecutor for concurrent scanning
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    # User input for host and port range
    target_host = input("Enter the target host (127.0.0.1, localhost, or scanme.nmap.org): ").strip()
    
    if not validate_target(target_host):
        print("Error: Invalid target host. You are only allowed to scan localhost or scanme.nmap.org.")
    else:
        try:
            start_port = int(input("Enter the starting port (1-65535): "))
            end_port = int(input("Enter the ending port (1-65535): "))
            
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                print("Error: Invalid port range. Ports must be between 1 and 65535.")
            else:
                # Run the port scanner
                port_scanner(target_host, start_port, end_port)
        except ValueError:
            print("Error: Please enter valid integers for ports.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
