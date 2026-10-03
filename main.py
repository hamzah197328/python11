while True:
    print("\n ---File operations menu---")
    print("1. create a file")
    print("2. Write to file")
    print("3. read file")
    print("4. Exit")
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        filename = input("Enter the filename to create your file: ")
        with open(filename, "w") as f:
            print(f"{filename} was made.")
    elif choice == "2":
        filename = input("Enter the filename to write to: ")
        with open(filename, "w") as f:
            content = input("Enter the content to write to the file: ")
            f.write(content)
            print(f"Content written to {filename} was delivered.")
    elif choice == "3":
        filename = input("Enter the filename to read: ")
        with open(filename, "r") as f:
            print(f"Contents of {filename}:")
            print(f.read())
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
