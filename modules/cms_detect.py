import subprocess

def scan(domain):
    try:
        result = subprocess.run(["whatweb", domain], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Failed to detect CMS: {result.stderr.strip()}"
    except Exception as e:
        return f"Error in CMS detection: {e}"