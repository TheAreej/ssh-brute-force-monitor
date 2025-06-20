import paramiko
from config import KALI_HOST, KALI_USER, KALI_PASSWORD, LOCAL_LOG_PATH
from datetime import datetime

def fetch_journal_logs():
    command = 'journalctl -u ssh --since "1 minute ago"'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(KALI_HOST, username=KALI_USER, password=KALI_PASSWORD)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            print(f"[!] Error fetching logs: {error}")
        else:
           
            with open(LOCAL_LOG_PATH, 'a', encoding='utf-8') as f:
                f.write(f"\n\n### Logs fetched at {datetime.now()} ###\n")
                f.write(output)
            print(" Log fetched successfully")

    except Exception as e:
        print(f" SSH Error: {e}")

    finally:
        ssh.close()
