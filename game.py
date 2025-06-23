import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors!")
while True:
   
    player_choice = input("\nChoose rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player_choice == "quit":
        print("Thanks for playing!")
        break
    if player_choice not in choices:
        print("Invalid choice. Please try again!")
        continue

    computer_choice = random.choice(choices)
    print(f"🤖 Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
