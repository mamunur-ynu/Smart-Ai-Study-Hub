def show_menu():
    print("\n Welcome to Smart AI Study Hub")
    print("Choose what you want to do today:")
    print("1. AI Note Summarizer")
    print("2. Vocabulary Builder")
    print("3. MCQ Generator")
    print("4. Speech to Text")
    print("5. Text to Speech")
    print("6. Study Timer (Pomodoro)")
    print("7. Local Offline Chatbot")
    print("0. Exit")

def main():
    while True: 
        show_menu()
        choice = input("Enter your option (0-7): ")

        if choice == "1":
            print("➡ Note summarizer: we will add the real feature here.\n")
        elif choice == "2":
            print("➡ Vocabulary builder: feature coming soon.\n")

        elif choice == "0":
            print("Thanks for using Smart AI Study Hub. Bye!")
            break
        else:
            print("Oops! Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
