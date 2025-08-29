import random

def get_choices():
    """Gets the user's choice and generates a random computer choice."""
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Input validation
    while user_choice not in options:
        user_choice = input("Invalid choice. Please enter 'rock', 'paper', or 'scissors': ").lower()
    
    computer_choice = random.choice(options)
    choices = {"user": user_choice, "computer": computer_choice}
    return choices

def determine_winner(user, computer):
    """Determines the winner based on the game logic."""
    if user == computer:
        return "It's a tie! 🤝"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win! 🎉"
    else:
        return "You lose! 😢"

def play_game():
    """Main function to run the game, track scores, and handle multiple rounds."""
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors! 🎮")
    
    while True:
        choices = get_choices()
        user_choice = choices["user"]
        computer_choice = choices["computer"]
        
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")
        
        # Update scores based on the result
        if "You win" in result:
            user_score += 1
        elif "You lose" in result:
            computer_score += 1
        
        print(f"Current Score: You - {user_score}, Computer - {computer_score}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You - {user_score}, Computer - {computer_score}")
            break

play_game()