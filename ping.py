# importing pythonping module
from pythonping import ping
# import save into file method
from utils import save_into_file



# ping host method
def ping_host(host):
    ping_result = ping(host, count=1, timeout=1)

    print(ping_result)

    return ping_result._responses[0].error_message is None



# ping handler
def ping_handler():
    host=input("[Host address] > ")

    if ping_host(host=host) == True:
        save_into_file("result_ping.txt", f"[ping result] < {host} is available.\n")
    else:
        save_into_file("result_ping.txt", f"[ping result] < {host} is not available.\n")
