                
import socket
import requests

# Port Scanner
def scan_ports(target):
    print(f"Scanning {target} for open ports...")
    for port in range(20, 1025):  # Scanning common ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            print(f"[+] Port {port} is open")
        s.close()

# SQL Injection Scanner
def check_sql_injection(url):
    payload = "' OR '1'='1' --"
    test_url = f"{url}?id={payload}"
    response = requests.get(test_url)
    
    if "error" in response.text.lower() or "sql" in response.text.lower():
        print(f"[!] {url} might be vulnerable to SQL injection!")
    else:
        print(f"[+] {url} seems safe.")

# Outdated Software Checker
def check_headers(url):
    response = requests.get(url)
    headers = response.headers
    if "server" in headers:
        print(f"Server Info: {headers['server']}")
        if "Apache/2.2" in headers['server']:  
            print("[!] Warning: This version of Apache is outdated!")

# Main Menu
print("1. Scan Open Ports")
print("2. Check for SQL Injection")
print("3. Check for Outdated Software")
choice = input("Choose an option (1/2/3): ")

if choice == "1":
    target_ip = input("Enter target IP: ")
    scan_ports(target_ip)
elif choice == "2":
    target_url = input("Enter website URL: ")
    check_sql_injection(target_url)
elif choice == "3":
    target_site = input("Enter website URL: ")
    check_headers(target_site)
else:
    print("Invalid choice!")
