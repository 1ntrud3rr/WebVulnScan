import socket

# Basic subdomain wordlist
subdomains = ["www", "mail", "ftp", "admin", "test", "webmail", "dev", "portal", "api", "vpn"]

def scan(domain):
    found = []

    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            found.append(f"[+] Found: {subdomain} → {ip}")
        except socket.gaierror:
            continue

    if not found:
        return "No common subdomains found.\n"
    return "\n".join(found)