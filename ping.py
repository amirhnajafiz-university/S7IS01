# importing pythonping module
from pythonping import ping


def ping_ip(ip):
    ping_result = ping(ip, count=1, timeout=1)
    print(ping_result)
    return ping_result._responses[0].error_message is None


def ping_handler():
    ip=input("Enter the domain you wish to ping : \n")
    if ping_ip(ip=ip) == True:
        print("#### {} is available. ###".format(ip))
    else:
        print("#### {} is not available. ####".format(ip))
