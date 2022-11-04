import nmap


def hostsiniprange(address):
    nm = nmap.PortScanner()
    nm.scan(address, arguments="-n -sP -PE -PA21,23,80,3389")
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print(f"{host} -> {status}")



def configureaddress(networkaddress, shost, ehost):
    address_split=networkaddress.split('.')[:3]
    address = ".".join(address_split)
    return f"{address}.{shost}-{ehost}"



def handlehostscanner():
    networkaddress = input("[Network address] > ")
    starting_host = input("Starting host > ")
    end_host = input("End host > ")
    address = configureaddress(networkaddress, starting_host, end_host)
    print(address)
    hostsiniprange(address=address)