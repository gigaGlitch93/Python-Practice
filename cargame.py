command = ""
started = False

while True:
    command = input(">").lower()

    if command == "start":
        if started:
            print("Car is already started. ")
        else:
            started = True
            print("Car Started...")

    elif command == "stop":
        if not started:
            print("Car is already Stopped.....")
        else:
            started = False
            print("Car stopped....")

    elif command == "help":
        print("""
start - to start the  car
stop - to stop the car
quit - to quit the game
        """)

    elif command == "quit":
        break

    else:
        print("I don't understand that. ")