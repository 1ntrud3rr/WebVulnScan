import argparse
import os
import json
import importlib
from tqdm import tqdm
from colorama import Fore, Style

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

def banner():
    print(f"""{Fore.CYAN}
██╗    ██╗███████╗██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██║    ██║██╔════╝██╔══██╗██║   ██║████╗  ██║██║ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██║ █╗ ██║█████╗  ██████╔╝██║   ██║██╔██╗ ██║█████╔╝ █████╗  ██║     ███████║██╔██╗ ██║
██║███╗██║██╔══╝  ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║     ██╔══██║██║╚██╗██║
╚███╔███╔╝███████╗██║     ╚██████╔╝██║ ╚████║██║  ██╗███████╗╚██████╗██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

                  Web Vulnerability Scanner by @aryanh4vks
{Style.RESET_ALL}""")

def main():
    banner()

    parser = argparse.ArgumentParser(description="Web Vulnerability Scanner")
    parser.add_argument("--domain", required=True, help="Target domain (example.com)")
    parser.add_argument("--format", choices=["txt", "json", "csv"], default=config["format"])
    parser.add_argument("--threads", type=int, default=config["threads"])
    parser.add_argument("--delay", type=float, default=config["delay"])
    parser.add_argument("--open", action="store_true", default=config["open"])
    args = parser.parse_args()

    domain = args.domain
    delay = args.delay
    threads = args.threads
    report_format = args.format
    auto_open = args.open

    print(f"\n[+] Starting scan on: {domain}\n")

    os.makedirs("output", exist_ok=True)
    report_path = f"output/scan_report_{domain}.{report_format}"

    results = {}  # for result correlation between modules

    with open(report_path, "w") as report:
        report.write(f"Scan Report for {domain}\n")
        report.write("="*50 + "\n\n")

        for mod_name in tqdm(config["enabled_modules"], desc="Running modules"):
            try:
                mod = importlib.import_module(f"modules.{mod_name}")
                if mod_name == "dir_brute":
                    result = mod.scan(domain, delay=delay, wordlist_path=config["wordlist"], threads=threads)
                else:
                    result = mod.scan(domain)
                results[mod_name] = result
                report.write(f"[{mod_name.replace('_', ' ').title()}]\n{result}\n\n")
            except Exception as e:
                report.write(f"[{mod_name}] Failed: {e}\n\n")

    print(f"\n[+] Scan completed! Report saved to {report_path}")
    if auto_open:
        os.system(f"xdg-open {report_path} || start {report_path} || open {report_path}")

if __name__ == "__main__":
    main()
