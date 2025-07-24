import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Referrer-Policy",
    "Permissions-Policy"
]

def scan(domain):
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=5)
        headers = response.headers
        report = []

        for header in SECURITY_HEADERS:
            if header in headers:
                report.append(f"[+] {header}: Present")
            else:
                report.append(f"[-] {header}: Missing")

        return "\n".join(report)
    except Exception as e:
        return f"Error fetching headers: {e}"