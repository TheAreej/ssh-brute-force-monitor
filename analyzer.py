from config import BRUTE_FORCE_THRESHOLD

def detect_brute_force(ip_attempts):
    return {ip: count for ip, count in ip_attempts.items() if count >= BRUTE_FORCE_THRESHOLD}
