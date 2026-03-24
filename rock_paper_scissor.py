def game_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "Player1 wins!"
    else:
        return "player2  wins!"

def main():
    player = input("Enter your choice player 1 (rock/paper/scissors): ").lower().strip()
    computer = input("Enter your choice player 2 (rock/paper/scissors): ").lower().strip()
    
    # FIXED: Print/display the result
    result = game_winner(player, computer)
    print(result)

if __name__ == "__main__":
    main()

