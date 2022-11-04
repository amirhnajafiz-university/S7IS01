# import nmap module.
import nmap
import time
# importing save into file function.
from utils import save_into_file



"""
Scan hosts with nmap and port scanner.
"""
def scan_hosts(address):
    nm = nmap.PortScanner()

    nm.scan(address, arguments="-n -sP -PE -PA21,23,80,3389")

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    save_into_file("result_host_scan.txt", f'{time.strftime("%H:%M:%S")}\n')

    for host, status in hosts_list:
        save_into_file("result_host_scan.txt", f"{host} => {status}\n")



"""
Host handler gets user data and scans the hosts with nmap.
"""
def host_handler():
    # get information from user
    network = input("[Network address] > ")
    st_host = input("[Starting host] > ")
    ed_host = input("[Ending host] > ")

    # making the address for nmap
    address= f"{'.'.join(network.split('.')[:3])}.{st_host}-{ed_host}"

    # calling host scanning method
    scan_hosts(address=address)