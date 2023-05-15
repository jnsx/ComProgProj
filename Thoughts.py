def thoughts(username):
    # THE TWITTER SYSTEM
    def load_thoughts(username):
        file_thoughts.seek(0)

        # Each line will be stripped and will be splitted by a colon
        for line in file_thoughts.readlines():
            user, thought = line.strip().split(":")
            # checks the logged user's thoughts/diary
            if username == user:
                thoughts.append(f'{thought}')

        print(f"You currently have {len(thoughts)} archives.\n")

    def write_thoughts(username):
        write = input("\nWhat's on your mind?\nW: >> >> ")
        file_thoughts.write(f"{username}:{write}\n")
        thoughts.append(write)
        print(
            "Press [W] to write a thought again or [R] to read your archives.\n")

    def read_thoughts(username):
        if len(thoughts) == 0:
            print("You currently have no archives.")
        else:
            print(f"\n>> >> {username} archives:")
            for i, j in enumerate(thoughts, 1):
                print(f"{i}. {j}")

        print("Press [W] to add something in your archives.\n")

    print(f"\n{username}: [W]rite [R]ead [S]ign out")

    thoughts = []

    with open('thoughts.txt', mode='a+', encoding='utf-8') as file_thoughts:
        load_thoughts(username)

        while True:
            command = input(">> >> ").upper()

            if command == "W":
                write_thoughts(username)

            elif command == "R":
                read_thoughts(username)

            elif command == "S":
                print("\n[L]ogin [R]egister [E]xit")
                break


def login_system():
    # THE LOGIN SYSTEM
    def load_registered_accounts(f):
        f.seek(0)

        # Reads each line of the file
        lines = f.readlines()
        for line in lines:
            # Each line will be stripped and will be splitted by a comma
            username, password = line.strip().split(",")

            # Username will be added to the set
            usernames.add(username)

            # Username and password will be stored in the dictionary
            accounts.setdefault(username, password)

    def login_an_account(username):

        # Checks if username already exists in the set usernames
        if username in usernames:
            # Prompt for the password
            password = input("Password: ")

            # Checks if password is correct
            if accounts[username] == password:
                print(f"Welcome {username}!")
                thoughts(username)
            else:
                print(
                    "Incorrect password!\nYou might wanna try again. Press [L] to try again or [R] to register an account")
        else:
            print(
                "Account doesn't exists.\nPress [L] to try again or [R] to register an account")

    def register_an_account(username):

        # Checks if username is already taken by another user
        if username in usernames:
            print("Username already taken")

        # Account being created
        else:
            usernames.add(username)
            password = input("password: ")
            accounts.setdefault(username, password)
            file.write(f"{username},{password}\n")
            print("Account created!\nYou can log in now.")

    usernames = set()
    accounts = {}

    # Automatically creates a file if doesn't exists
    with open('accounts.db', mode='a+', encoding="utf-8") as file:
        # Read the file and loads the registered accounts if there are any
        load_registered_accounts(file)

        print("[L]ogin [R]egister [E]xit")

        while True:
            command = input("\n>> ").upper()

            if command == "L":
                username = input("Username: ")
                login_an_account(username)

            elif command == "R":
                print("Creating an account:")
                username = input("Username: ")
                register_an_account(username)

            elif command == "E":
                break


login_system()