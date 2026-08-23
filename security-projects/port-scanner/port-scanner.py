import socket
import time
import ipaddress
import sys
import threading

MAX_THREADS = 200
TIME_OUT = 1.5
SHOW_PROGRESS = True

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def port_scanner(ip,port,open_ports) :
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(TIME_OUT)
        result = sock.connect_ex((ip,port))
        if result == 0:
            open_ports.append(port)
            print(f"\033[92m[+] پورت {port} در {ip} بازه\033[0m")
        sock.close()
    except ValueError:
        pass
def main():
    print("Simple Port Scanner - شروع اسکن...\n")

    target = input("لطفاً IP یا دامنه را وارد کنید : ").strip()
    try:
        if not is_valid_ip(target):
            target = socket.gethostbyname(target)
            print(f" دامنه تبدیل شد به: {target}")
    except socket.gaierror:
        print(" دامنه یا IP نامعتبر است")
        sys.exit(1)
    start_port = int(input("از پورت (پیش‌فرض ۱): ") or "1")
    end_port = int(input("تا پورت (پیش‌فرض 65535): ") or "65535")
    num_threads = int(input("تعداد thread همزمان (پیش‌فرض 200): ") or MAX_THREADS)
    open_ports = []
    total_ports = end_port - start_port + 1
    start_time = time.time()

    threads = []
    for port in range(start_port,end_port + 1 ):
        if len(threads) >= num_threads or port == end_port:
            for t in threads :
                t.start()
            for t in threads:
                t.join()
            threads.clear()
        thread = threading.Thread(target=port_scanner,args=(target,port,open_ports) or MAX_THREADS)
        threads.append(thread)
    open_ports = sorted(open_ports)
    elapsed = time.time() - start_time
    print("\n" + "=" * 50)
    print(f" اسکن تمام شد! {len(open_ports)} پورت باز از {total_ports}")
    print(f" زمان کل: {elapsed:.2f} ثانیه")
    print("=" * 50)
    if open_ports:
        print("\n پورت‌های باز:")
        for p in open_ports:
            print(f"   پورت {p}")
    else:
        print("\n هیچ پورت باز یافت نشد.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ اسکن توسط کاربر لغو شد.")