print("Welcome to Tanay's Launch Console!")

user_name = input("What is your name? ")
print(f"Hi, {user_name}! Welcome to my Launch Console.")

running = True

while running:
    print("\nMenu")
    print("1. About me")
    print("2. My goals")
    print("3. My favorite project")
    print("4. Fun fact")
    print("5. Exit")

    choice = input("Choose an option from 1 to 5: ")

    if choice == "1":
        print("My name is Tanay. I am a student who enjoys technology, robotics, and learning new things.")

    elif choice == "2":
        print("My goals are to improve my coding skills, do well in school, and create useful projects.")

    elif choice == "3":
        print("My favorite project is creating a system that detects, tracks, and predicts the movement of a tennis ball.")

    elif choice == "4":
        print("A fun fact about me is that I enjoy building and designing robots.")

    elif choice == "5":
        print(f"Goodbye, {user_name}! Thanks for using my Launch Console.")
        running = False

    else:
        print("Please enter a valid option from 1 to 5!")