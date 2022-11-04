from ping import ping_handler



# enums of the project
PING_COMMAND = "ping"
HOST_COMMAND = "host scan"
PORT_COMMAND = "port scan"
EXIT_COMMAND = "exit"



# showing the project menu
def menu():
    print(f"1. {PING_COMMAND}")
    print(f"2. {HOST_COMMAND}")
    print(f"3. {PORT_COMMAND}")
    print(f"4. {EXIT_COMMAND}")
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
            pass
        elif cmd == PORT_COMMAND:
            pass
        elif cmd == EXIT_COMMAND:
            break
        else:
            print("! Wrong input")
