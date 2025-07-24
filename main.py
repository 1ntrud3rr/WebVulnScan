
import argparse
import os
from modules import port_scan, dir_brute, vuln_scan, cms_detect, headers_check, subdomains


def banner():
    print("""
██╗    ██╗███████╗██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██║    ██║██╔════╝██╔══██╗██║   ██║████╗  ██║██║ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝██║   ██║██╔██╗ ██║█████╔╝ █████╗  ██║     ███████║██╔██╗ ██║
██║███╗██║██╔══╝  ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║     ██╔══██║██║╚██╗██║
╚███╔███╔╝███████╗██║     ╚██████╔╝██║ ╚████║██║  ██╗███████╗╚██████╗██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

                     Web Vulnerability Scanner by @aryanh4vks
    """)


def main():
    banner()
    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("--domain", required=True, help="Target domain (example.com)")
    args = parser.parse_args()
    domain = args.domain

    print(f"\n[+] Starting scan on: {domain}\n")

    # Create output directory
    os.makedirs("output", exist_ok=True)
    report_path = f"output/scan_report_{domain}.txt"

    with open(report_path, "w") as report:
        report.write(f"Scan Report for {domain}\n")
        report.write("="*50 + "\n\n")

        # Port Scan
        result = port_scan.scan(domain)
        report.write("[Port Scan]\n" + result + "\n")

        # CMS Detection
        result = cms_detect.scan(domain)
        report.write("[CMS Detection]\n" + result + "\n")

        # Directory Bruteforce
        result = dir_brute.scan(domain)
        report.write("[Directory Bruteforce]\n" + result + "\n")

        # Header Security Check
        result = headers_check.scan(domain)
        report.write("[Header Security Check]\n" + result + "\n")

        # Subdomain Enumeration
        result = subdomains.scan(domain)
        report.write("[Subdomain Enumeration]\n" + result + "\n")

        # Vuln Scan Placeholder
        result = vuln_scan.scan(domain)
        report.write("[Known Vulnerabilities]\n" + result + "\n")

    print(f"\n[+] Scan completed! Report saved to {report_path}")


if __name__ == "__main__":
    main()
