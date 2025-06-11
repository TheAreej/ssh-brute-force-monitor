```markdown
# SSH Brute Force Monitor

A modular Python-based tool to monitor SSH logs, detect brute force attacks, send email alerts, and visualize failed login attempts. Designed to help blue teamers detect and respond to suspicious SSH activity in real-time.

---

##  Features

- Monitors SSH logs for failed login attempts.
- Detects brute force attacks using a configurable threshold.
- Sends real-time email alerts.
- Checks IP reputation using [AbuseIPDB](https://abuseipdb.com).
- Generates reports and visualizations:
  - Text report of login activity.
  - Bar charts showing attempts by IP and by username.

---

##  Project Structure

```
SSH-BruteForce-Monitor/
│
├── logs/                     # Folder to store SSH log files
├── reports/                  # Output: charts and reports
│
├── analyzer.py               # Analyzes parsed data for brute force activity
├── config.py                 # Email, log directory, and API configuration
├── main.py                   # Entry point: runs the full monitoring loop
├── notifier.py               # Sends email alerts
├── parser.py                 # Parses SSH logs and extracts login attempts
├── visualizer.py             # Generates charts from data
│
├── README.md                 # Project documentation (this file)
└── requirements.txt          # List of required Python packages
```

---

##  Requirements

- Python 3.7+
- Install dependencies:

```bash
pip install -r requirements.txt
```

### Python Libraries Used

- `matplotlib`
- `requests`
- `smtplib` (built-in)
- `email` (built-in)
- `re`, `os`, `time`, `collections` (built-in)

---

##  Configuration

Edit `config.py` to set your credentials and paths:

```python
EMAIL_SENDER = 'youremail@gmail.com'
EMAIL_APP_PASSWORD = 'your_app_password'
EMAIL_RECEIVER = 'receiver@example.com'

API_KEY = 'your_abuseipdb_api_key'

BRUTE_FORCE_THRESHOLD = 3
LOGS_DIR = './logs'  # or path to /var/log/auth.log
```

---

##  How to Run

1. Add SSH log files to the `logs/` directory.
2. Run the main script:

```bash
python3 main.py
```

3. The tool will:
   - Parse logs
   - Detect suspicious IPs
   - Send email alerts
   - Generate `report.txt` and visual charts in `reports/`

---

##  Output Files

- `reports/report.txt` — Summary of login attempts and alerts
- `reports/ip_attempts_chart.png` — Failed attempts by IP
- `reports/user_attempts_chart.png` — Failed attempts by username

---

##  Example Log Format (from `/var/log/auth.log`)

```
Failed password for invalid user test from 192.168.1.5 port 22 ssh2
Failed password for root from 203.0.113.50 port 22 ssh2
```

---

##  Future Enhancements

- Telegram or Discord alert support
- SQLite database for log history
- Web dashboard for live monitoring
- GeoIP location visualization

---

##  Author's Note

This project is a learning tool for cybersecurity enthusiasts, blue teamers, and SOC analysts. Feedback and contributions are welcome!
