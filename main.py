def show_menu():
    """Prints the main menu options for the Smart AI Study Hub."""
    print("\n--- SMART AI STUDY HUB ---")
    print("What do you want to do today?")
    print("1. AI Note Summarizer")
    print("2. Vocabulary Builder")
    print("3. MCQ Generator")
    print("4. Speech to Text")
    print("5. Text to Speech")
    print("6. Study Timer (Pomodoro)")
    print("7. Local Offline Chatbot")
    print("0. Exit")
    print("--------------------------")


def main():
    """Handles the user input loop and feature selection."""
    while True:
        show_menu()

        choice = input("Enter your option (0-7): ")

        if choice == "1":
            print("-> AI Note Summarizer selected. We will add the real feature here.\n")

        elif choice == "2":
            print("-> Vocabulary Builder selected. Feature coming soon.\n")

        elif choice == "3":
            print("-> MCQ Generator selected. Feature coming soon.\n")

        elif choice == "4":
            print("-> Speech to Text selected. Feature coming soon.\n")

        elif choice == "5":
            print("-> Text to Speech selected. Feature coming soon.\n")

        elif choice == "6":
            print("-> Study Timer (Pomodoro) selected. Feature coming soon.\n")

        elif choice == "7":
            print("-> Local Offline Chatbot selected. Feature coming soon.\n")

        elif choice == "0":
            print("Thanks for using Smart AI Study Hub. Bye!")
            break

        else:
            print("-> Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
