import time
from fetcher import fetch_journal_logs
from parser import parse_logs
from analyzer import detect_brute_force
from notifier import send_alert

alerted_ips = set()

while True:
    print("Checking for SSH logs...")
    
    fetch_journal_logs()
    
    ip_attempts, user_attempts = parse_logs()
    brute_force_ips = detect_brute_force(ip_attempts)
    
    for ip, count in brute_force_ips.items():
        if ip not in alerted_ips:
            send_alert(ip, count)
            alerted_ips.add(ip)
            print(f"Alert sent for {ip}")
    
    print("Waiting for 60 seconds...\n")
    time.sleep(60)
