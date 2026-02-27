users = []

while True:
    print("\n==== USER MANAGEMENT SYSTEM ====")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    
    if choice == "1":
        if len(users) == 0:
            print("No users found.")
        else:
            print("\nUser List:")
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")

    
    elif choice == "2":
        new_user = input("Enter new user name: ")
        users.append(new_user)
        print("User added successfully.")

    
    elif choice == "3":
        if len(users) == 0:
            print("No users to update.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            num = int(input("Enter user number to update: "))
            if 1 <= num <= len(users):
                updated_name = input("Enter new name: ")
                users[num - 1] = updated_name
                print("User updated successfully.")
            else:
                print("Invalid number.")

    
    elif choice == "4":
        if len(users) == 0:
            print("No users to delete.")
        else:
            for i in range(len(users)):
                print(f"{i + 1}. {users[i]}")
            num = int(input("Enter user number to delete: "))
            if 1 <= num <= len(users):
                users.pop(num - 1)
                print("User deleted successfully.")
            else:
                print("Invalid number.")

    
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
