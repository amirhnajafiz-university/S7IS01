# import handlers from files
from ping import ping_handler
from host import host_handler
from port import ports_handler



# enums of the project
PING_COMMAND = "ping"
HOST_COMMAND = "host scan"
PORT_COMMAND = "port scan"
EXIT_COMMAND = "exit"



# showing the project menu
def menu():
    print()
    print(f"* {PING_COMMAND}")
    print(f"* {HOST_COMMAND}")
    print(f"* {PORT_COMMAND}")
    print(f"* {EXIT_COMMAND}")
    print()



# main loop
if __name__ == "__main__":
    while True:
        # display menu
        menu()
        # get user input
        cmd = input("> ")
        # check input
        if cmd == PING_COMMAND:
            ping_handler()
        elif cmd == HOST_COMMAND:
            host_handler()
        elif cmd == PORT_COMMAND:
            ports_handler()
        elif cmd == EXIT_COMMAND:
            break
        else:
            print("< Wrong input!")
