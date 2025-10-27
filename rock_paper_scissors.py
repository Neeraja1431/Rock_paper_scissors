# rock_paper_scissors.py
import random

def play_game():
    options = ["rock", "paper", "scissors"]
    print("✨ Welcome to Neeru's Rock–Paper–Scissors Game ✨")

    while True:
        user_choice = input("\nEnter your choice (rock/paper/scissors or 'quit' to exit): ").lower()

        if user_choice == "quit":
            print("👋 Thanks for playing! Bye Neeru 💖")
            break

        if user_choice not in options:
            print("❌ Invalid choice! Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"🧍 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

# ---------- Main Program ----------
if __name__ == "__main__":
    play_game()
