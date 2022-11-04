import nmap



def scanports(address, sport, eport):
    nm = nmap.PortScanner()
    nm.scan(address, f"{sport}-{eport}")
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname))
        print('State: %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print("Proto: %s" % proto)

            lport = nm[host][proto].keys()
            for port in lport:
                print(f"port {port} : {nm[host][proto][port]}")



def handleportscan():
    network = input()
    start = input()
    stop = input()
    scanports(network, start, stop)