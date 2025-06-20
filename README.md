ممتاز، الـ `README.md` السابق منظّم وواضح جدًا. وبما أنك أرسلت لي هذا، يبدو أنك ترغب بمراجعته أو تعديله بما يتناسب مع مشروعك الحالي.

إليك نسخة محسّنة قليلًا من نفس النص مع بعض التعديلات اللغوية الطفيفة لتكون أكثر احترافية، ودون تغيير الهيكل العام:

---

```markdown
# SSH Brute Force Monitor

A modular Python-based tool to monitor SSH logs, detect brute-force attacks, send email alerts, and visualize failed login attempts. Designed to help blue teamers detect and respond to suspicious SSH activity in real-time.

---

## Features

- Monitors SSH logs for failed login attempts
- Detects brute-force attacks using a configurable threshold
- Sends real-time email alerts
- Checks IP reputation using [AbuseIPDB](https://abuseipdb.com)
- Generates reports and visualizations:
  - Text-based activity report
  - Bar charts showing login attempts by IP and by username

---

## Project Structure

```

SSH-BruteForce-Monitor/
│
├── logs/                     # Folder to store raw SSH log files
├── reports/                  # Output: reports and visualizations
│
├── analyzer.py               # Detects brute-force activity
├── config.py                 # Contains configuration variables
├── main.py                   # Main execution script
├── notifier.py               # Handles email notifications
├── parser.py                 # Extracts login attempts from logs
├── visualizer.py             # Generates visual charts
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

````

---

## Requirements

- Python 3.7 or higher

Install dependencies with:

```bash
pip install -r requirements.txt
````

### Python Libraries Used

* `matplotlib`
* `requests`
* Built-in: `smtplib`, `email`, `re`, `os`, `time`, `collections`

---

## Configuration

Edit `config.py` to match your setup:

```python
EMAIL_SENDER = 'youremail@gmail.com'
EMAIL_APP_PASSWORD = 'your_app_password'
EMAIL_RECEIVER = 'receiver@example.com'

API_KEY = 'your_abuseipdb_api_key'

BRUTE_FORCE_THRESHOLD = 3
LOGS_DIR = './logs'  # or path to /var/log/auth.log
```

---

## How to Run

1. Place SSH log files in the `logs/` directory.
2. Run the main script:

```bash
python3 main.py
```

3. The tool will:

   * Parse SSH logs
   * Identify suspicious IPs
   * Send alert emails
   * Generate `report.txt` and charts in the `reports/` directory

---

## Output Files

* `reports/report.txt` — Summary of login attempts and detected threats
* `reports/ip_attempts_chart.png` — Failed login attempts by IP
* `reports/user_attempts_chart.png` — Failed login attempts by username

---

## Example Log Entry (from `/var/log/auth.log`)

```
Failed password for invalid user test from 192.168.1.5 port 22 ssh2
Failed password for root from 203.0.113.50 port 22 ssh2
```

---

## Future Enhancements

* Telegram or Discord alert integration
* SQLite database support for historical tracking
* Web-based dashboard for real-time monitoring
* GeoIP-based visual mapping

---

## Author's Note

This project serves as a learning and defensive security tool for blue teamers, SOC analysts, and cybersecurity students. Contributions and suggestions are welcome.


