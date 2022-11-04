# importing pythonping module
from pythonping import ping
# import save into file method
from utils import save_into_file



# constants
OUTPUT_FILE = "result_ping.txt"



# ping host method
def ping_host(host):
    ping_result = ping(host, count=1, timeout=1)

    save_into_file(OUTPUT_FILE, f"{ping_result.__str__()}\n")

    return ping_result._responses[0].error_message is None



# ping handler
def ping_handler():
    host=input("[Host address] > ")

    if ping_host(host=host) == True:
        save_into_file(OUTPUT_FILE, f"{host} is available.\n")
    else:
        save_into_file(OUTPUT_FILE, f"{host} is not available.\n")
    
    print(f'< Results are in {OUTPUT_FILE}')
