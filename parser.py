import re
from collections import defaultdict
from config import LOCAL_LOG_PATH

def parse_logs():
    ip_attempts = defaultdict(int)
    user_attempts = defaultdict(int)

    pattern = re.compile(r'Failed password for (invalid user )?(\S+) from ([\d\.]+)')

    try:
        with open(LOCAL_LOG_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                match = pattern.search(line)
                if match:
                    user = match.group(2)
                    ip = match.group(3)
                    ip_attempts[ip] += 1
                    user_attempts[user] += 1

    except FileNotFoundError:
        print("Log file not found yet.")

    return ip_attempts, user_attempts
