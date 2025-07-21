import random

def get_user_choice():
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
    return choices.get(choice, None)

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def main():
    print("=== 🎮 Rock Paper Scissors Game ===")
    while True:
        user_choice = get_user_choice()
        if not user_choice:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()

        print(f"\n🧍 You chose: {user_choice}")
        print(f"🤖 Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(f"\n🏁 Result: {result}")

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
