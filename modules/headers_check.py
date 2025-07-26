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
        url = domain if domain.startswith("http") else f"https://{domain}"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; WebVulnScan/1.0)"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response_headers = response.headers

        report = []
        for header in SECURITY_HEADERS:
            if header in response_headers:
                report.append(f"[+] {header}: Present")
            else:
                report.append(f"[-] {header}: Missing")

        return "\n".join(report)

    except Exception as e:
        return f"Error fetching headers: {e}"