
import os
import re
from collections import defaultdict
from config import LOGS_DIR

def parse_logs():
    ip_attempts = defaultdict(int)
    user_attempts = defaultdict(int)

    pattern = re.compile(r'Failed password for (invalid user )?(\w+) from ([\d.]+)')

    for fname in os.listdir(LOGS_DIR):
        if fname.endswith('.log'):
            with open(os.path.join(LOGS_DIR, fname), 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    match = pattern.search(line)
                    if match:
                        user = match.group(2)
                        ip = match.group(3)
                        ip_attempts[ip] += 1
                        user_attempts[user] += 1

    return ip_attempts, user_attempts
