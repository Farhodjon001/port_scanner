import socket,threading
from datetime import datetime
try:
    host = ("localhost")
    host_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Host topilmadi")

threds = []
open_ports = {}

def check_ports(ip, port, delay,open_ports):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
            sock.settimeout(delay)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports[port] = "open"

    except:
        pass

def scanning_ports(host_ip,delay):
    for port in range(1,65535):
        thread = threading.Thread(target=check_ports, args=(host_ip, port, delay, open_ports))
        threds.append(thread)

    for i in range(0,65534):
        threds[i].start()

    for i in range(0,65534):
        threds[i].join

    for key, value in open_ports.items():
        print(f"Open port:{str(key)}")
start_time = datetime.now()
scanning_ports(host_ip,0.001)
end_time = datetime.now()
print(f"Total_time : {end_time-start_time}")





