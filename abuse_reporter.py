import requests
from config import ABUSEIPDB_API_KEY

def report_to_abuseipdb(ip):
    url = 'https://api.abuseipdb.com/api/v2/report'
    headers = {
        'Key': ABUSEIPDB_API_KEY,
        'Accept': 'application/json'
    }
    data = {
        'ip': ip,
        'categories': '18',  # SSH brute force
        'comment': 'Detected SSH brute-force via custom log analyzer.'
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except Exception as e:
        print(f" Error reporting IP {ip} to AbuseIPDB: {e}")
        return None
