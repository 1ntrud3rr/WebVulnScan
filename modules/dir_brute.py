import requests

# A small default wordlist
wordlist = ["admin", "login", "dashboard", "config", "uploads", "backup", "test", "panel"]

def scan(domain):
    found = []
    base_url = f"http://{domain}"  # or https, can make this dynamic later

    for word in wordlist:
        url = f"{base_url}/{word}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 301, 302]:
                found.append(f"[+] Found: {url} (Status: {response.status_code})")
        except requests.RequestException:
            continue

    if not found:
        return "No common directories found.\n"
    return "\n".join(found)