# importing pythonping module
from pythonping import ping



# ping host method
def ping_host(host):
    ping_result = ping(host, count=1, timeout=1)

    print(ping_result)

    return ping_result._responses[0].error_message is None



# ping handler
def ping_handler():
    host=input("[Host address] > ")

    if ping_host(host=host) == True:
        print(f"[ping result] < {host} is available.")
    else:
        print(f"[ping result] < {host} is not available.")
