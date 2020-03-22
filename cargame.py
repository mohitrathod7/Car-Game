cond = True
is_started = False
is_stopped = True
while cond == True:
    msg = input('>').lower()
    if msg == "help":
        print("start-to start car     stop-to stop car     quit-to exit")
    elif msg == "start":
        if is_started == True and is_stopped == False:
            print("Car has already started.")
        if is_started == False and is_stopped == True:
            print("Car started.")
            is_started = True
            is_stopped = False
    elif msg == "stop":
        if is_started == True and is_stopped == False:
            print("Car stopped.")
            is_started = False
            is_stopped = True
        elif is_started == False and is_stopped == True:
            print("Car has already stopped.")
    elif msg == "status":
        print("Status : is_started =", is_started, "and is_stopped =", is_stopped)
    elif msg == "quit":
        cond = False
    else:
        print("I dont understand that......")
