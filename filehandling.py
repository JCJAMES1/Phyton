try:
    file = open ("message.txt", "x")
    print("File Created Successfully!")
except FileExistsError:
    print("File Already Exist")

while True:
    print("\n1. Send a message: ")
    print("2. View all message: ")
    print("3. Exit: ")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        try:
            message = input("Enter your message: ")
            file = open("message.txt", "a")
            file.write(message + "\n")
            file.close()
            print("Message sent Successfully!")
        except Exception as e:
            print("Error while sending message")
            
    elif choice == "2":
        try:
            file = open ("message.txt", "r")
            content = file.read()
            print("Your messages: ")
            print(content)
            file.close()
            
        except FileNotFoundError:
            print("File not found")
    elif choice == "3":
        print("Thankyou for exiting the program")
        break
    
    else:
        print("Error please try again")
    
