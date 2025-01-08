import socket
import subprocess
from collections import defaultdict
import time
import argparse

# Set the threshold values
INITIAL_BLOCK_THRESHOLD = 50  # Requests allowed before blocking
POST_BLOCK_LIMIT = 10         # Requests allowed during cooldown

# Parse cooldown period from command line
parser = argparse.ArgumentParser(description='Set the cooldown period for blocked IPs.')
parser.add_argument('--cooldown', type=int, required=True, help='Cooldown period in seconds.')
args = parser.parse_args()
COOLDOWN_PERIOD = args.cooldown

# Track request counts and blocked IPs
request_counts = defaultdict(int)
blocked_ips = {}

def block_ip_windows(ip):
    """Block IP using Windows Firewall."""
    if ip not in blocked_ips:
        try:
            command = f"powershell -Command \"New-NetFirewallRule -DisplayName Block_{ip} -Direction Inbound -RemoteAddress {ip} -Action Block\""
            subprocess.run(command, shell=True)
            print(f"Blocked IP: {ip}")
            blocked_ips[ip] = {'start_time': time.time(), 'request_count': 0}
        except Exception as e:
            print(f"Failed to block IP {ip}: {e}")

def unblock_ip(ip):
    """Unblock the IP address."""
    try:
        command = f"powershell -Command \"Remove-NetFirewallRule -DisplayName Block_{ip}\""
        subprocess.run(command, shell=True)
        print(f"Unblocked IP: {ip}")
        del blocked_ips[ip]
    except Exception as e:
        print(f"Failed to unblock IP {ip}: {e}")

def monitor_requests():
    """Monitor requests and manage blocking."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(5)
    server_socket.settimeout(1)

    try:
        while True:
            try:
                client_socket, client_address = server_socket.accept()
                ip = client_address[0]

                # Cooldown logic for blocked IPs
                if ip in blocked_ips:
                    blocked_ips[ip]['request_count'] += 1
                    elapsed_time = time.time() - blocked_ips[ip]['start_time']
                    if elapsed_time < COOLDOWN_PERIOD:
                        if blocked_ips[ip]['request_count'] > POST_BLOCK_LIMIT:
                            print(f"Blocked IP {ip} exceeded POST_BLOCK_LIMIT.")
                    else:
                        if blocked_ips[ip]['request_count'] <= POST_BLOCK_LIMIT:
                            unblock_ip(ip)
                else:
                    # Monitor and block based on threshold
                    request_counts[ip] += 1
                    print(f"Request from IP: {ip} - Count: {request_counts[ip]}")
                    if request_counts[ip] > INITIAL_BLOCK_THRESHOLD:
                        block_ip_windows(ip)
                        request_counts[ip] = 0

                client_socket.close()
            except socket.timeout:
                # Check if cooldown period has expired
                for ip in list(blocked_ips.keys()):
                    elapsed_time = time.time() - blocked_ips[ip]['start_time']
                    if elapsed_time >= COOLDOWN_PERIOD:
                        unblock_ip(ip)

    except KeyboardInterrupt:
        print("Shutting down server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    monitor_requests()

---