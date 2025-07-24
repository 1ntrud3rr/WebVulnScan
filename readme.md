# WebVulnScan

**A powerful and modular web vulnerability scanner built in Python.**

![Banner](https://github.com/aryanh4cks/WebVulnScan/assets/banner.png)

## 🔥 Features

- 🔍 Port scanning
- 🧠 CMS detection
- 🗂️ Directory bruteforcing with threading
- 🛡️ Header security checks
- 🌐 Subdomain enumeration
- 🚨 Known vulnerability detection
- ⚙️ Nmap integration
- 🧱 WAF detection
- 📄 Multi-format output (TXT/JSON/CSV)
- ⚡ Threading, delays & verbosity options
- 🧪 Test mode & auto-preview support

---

## 📦 Installation

```bash
# Clone the repository
https://github.com/aryanh4cks/WebVulnScan.git
cd WebVulnScan

# Install Python dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python3 main.py --domain example.com \
                --format json \
                --verbose \
                --delay 0.2 \
                --threads 15 \
                --open
```

### ✅ Test Mode
```bash
python3 main.py --test
```
Runs all modules against `example.com` to verify functionality.

---

## 📁 Output
- Reports are saved under the `output/` folder.
- File name format: `scan_report_<domain>.<format>`
- Formats: `.txt`, `.json`, `.csv`

---

## 🛠 Modules Overview
- `port_scan`: Open port and service enumeration
- `dir_brute`: Threaded brute-forcing of directories
- `cms_detect`: CMS and fingerprint detection
- `headers_check`: Identifies missing security headers
- `subdomains`: Subdomain brute-force discovery
- `vuln_scan`: Detects known/basic vulnerability signatures

---

## 🧪 Testing
Run all modules with pytest:
```bash
pytest test_webvulnscan.py
```

---

## 📜 License
MIT License

---

## 👤 Author
**[@aryanh4cks](https://github.com/aryanh4cks)**

> Built with ❤️ for ethical hacking and security research.
