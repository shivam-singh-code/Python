import sys
import random
from enum import Enum

def rps(name="PlayerOne"):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerChoice = input(f"\n{name}, please Enter... \n1 for Rock,\n2 for Paper, or\n3 for scissors:\n\n")

        if playerChoice not in ["1", "2", "3"]:
            print(f"{name}, Please You must enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerChoice)

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        print("")
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.','').title()} .")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you Win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you Win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, you Win"
            elif player == computer:
                return "Tie Game"
            else:
                python_wins += 1
                return f"Python wins!nSorry, {name}..😢"
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        
        print(f"\n Game Count: {game_count}")
        print(f"\n {name} Wins: {player_wins}")
        print(f"\n Python Wins: {python_wins}")
        print(f"\nPlay again, {name}?")

        while True:
            playAgain = input('\n Enter y to play again \n Enter q to quit\n')
            if playAgain.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if playAgain.lower() == "y":
            return play_rps()
        else:
            print("🎉🎉🎉🎉")
            print("Thankyou for playing😊")
            sys.exit(f'Bye {name}! 👍')

    return play_rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provide a personalized game experience.")
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
