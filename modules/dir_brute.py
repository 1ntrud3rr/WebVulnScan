import requests
import threading
import time

def scan(domain, delay=0, wordlist_path=None, threads=10):
    discovered_paths = []
    lock = threading.Lock()

    if wordlist_path:
        try:
            with open(wordlist_path, 'r') as file:
                paths = [line.strip() for line in file if line.strip()]
        except Exception as e:
            return f"[ERROR] Failed to load wordlist: {e}"
    else:
        paths = ["admin", "login", "dashboard", "config", "upload", "server-status"]

    def worker(path):
        url = f"http://{domain}/{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 301, 302]:
                with lock:
                    discovered_paths.append(f"{url} [{response.status_code}]")
        except requests.RequestException:
            pass
        time.sleep(delay)

    threads_list = []
    for path in paths:
        t = threading.Thread(target=worker, args=(path,))
        threads_list.append(t)
        t.start()
        if len(threads_list) >= threads:
            for t in threads_list:
                t.join()
            threads_list = []

    for t in threads_list:
        t.join()

    if discovered_paths:
        return "\n".join(discovered_paths)
    return "No directories discovered."