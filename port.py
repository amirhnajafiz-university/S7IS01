# import nmap module.
import nmap
# import save into files method.
from utils import save_into_file



# constants
OUTPUT_FILE = "result_ports_scan.txt"



"""
Scan ports with nmap.
"""
def scan_ports(address, st_port, ed_port):
    nm = nmap.PortScanner()

    nm.scan(address, f"{st_port}-{ed_port}")

    for host in nm.all_hosts():
        ctx = ""
        ctx += f'host: {host} / {nm[host].hostname()}\n'
        ctx += f'state: {nm[host].state()}\n'
        for protocol in nm[host].all_protocols():
            ctx += f'# protocol: {protocol}\n'
            for port in nm[host][protocol].keys():
                ctx += f"port {port} : {nm[host][protocol][port]}\n"
        ctx += "####\n"

        save_into_file(OUTPUT_FILE, ctx)



"""
Scan ports.
"""
def ports_handler():
    network = input("[Network address] > ")
    start = input("[Starting port] > ")
    stop = input("[Ending port] > ")

    scan_ports(network, start, stop)

    print(f'< Results are in {OUTPUT_FILE}')