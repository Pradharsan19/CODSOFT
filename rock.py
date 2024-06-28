import random

# Define the possible choices
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        # Prompt user for their choice
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").strip().lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Generate computer's random choice
        computer_choice = random.choice(choices)
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display choices and result
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display scores
        print(f"\nScores -> You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
