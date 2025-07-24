import nmap

def scan(domain):
    try:
        nm = nmap.PortScanner()
        nm.scan(domain, arguments='-T4 -F')  # Fast scan
        output = ""
        for host in nm.all_hosts():
            output += f"Host: {host} ({nm[host].hostname()})\n"
            output += f"State: {nm[host].state()}\n"
            for proto in nm[host].all_protocols():
                output += f"Protocol: {proto}\n"
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    state = nm[host][proto][port]['state']
                    output += f"  Port: {port}, State: {state}\n"
        return output if output else \"No open ports found.\\n\"
    except Exception as e:
        return f\"Error during port scan: {e}\\n\"