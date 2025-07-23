import random

WINNING_SCORE = 50

def roll_die():
    return random.randint(1, 6)

def get_player_count():
    while True:
        num = input(f"Enter number of players (1-4): ")
        if num.isdigit():
            num = int(num)
            if 1 <= num <= 4:
                return num
            
        print("Invalid input. Please try again.")


def is_human(player_id, human_count):
    return player_id < human_count


def gamble_double_or_nothing(score, machine=False):
    if score == 0:
        return 0

    if machine:

        if score >= 6 and random.random() < 0.5:
            print("Bot chooses to gamble...")

            if random.choice([True, False]):
                print("Bot doubled its turn score!")
                return score * 2
            else:
                print("Bot lost everything on the gamble!")
                return 0
        else:
            print("Bot plays it safe.")
            return score
        
    else:
        print("\n DOUBLE OR NOTHING TIME!")

        gamble = input("Do you want to gamble your turn points? (y/n): ").lower()

        if gamble == "y":

            if random.choice([True, False]):
                print("Success! You doubled your turn score!")
                return score * 2
            else:
                print("Oof! You lost everything from this turn!")
                return 0
        else:
            print("Safe choice! Keeping your turn score.")
            return score
        

def player_turn(player_id, current_total, machine_player):
    print(f"\n Player {player_id + 1}'s turn!")
    print(f"Total score: {current_total}")
    turn_score = 0

    while True:
        if machine_player:
            if turn_score >= 14 :
                print("Bot holds.")
                break
            print("Bot rolls...")
        else:
            choice = input("Roll the die? (y): ").lower()
            if choice != "y":
                break

        roll = roll_die()
        print(f"Rolled: {roll}")

        if roll == 1:
            print("Rolled a 1! Turn done! No points this turn.")
            return 0
        else:
            turn_score += roll
            print(f"Turn score: {turn_score}")

    return gamble_double_or_nothing(turn_score, machine_player)

def display_scores(scores, num_humans):
    print("\nCurrent Scores:")
    for i, score in enumerate(scores):
        if num_humans == len(scores):
            player_label = f"Player {i + 1}"
        else:
            player_label = "You" if is_human(i, num_humans) else f"Bot"

        print(f"{player_label}: {score}")
    print("--------------------------")

def main():
    print("Welcome to the Pig Dice Game!")

    num_players = get_player_count()

    if num_players == 1:
        print("Adding 1 AI opponent for solo play.")
        num_players = 2
        num_humans = 1
    else:
        num_humans = num_players

    scores = [0] * num_players

    while max(scores) < WINNING_SCORE:

        for i in range(num_players):

            is_machine = not is_human(i, num_humans)

            turn_points = player_turn(i, scores[i], is_machine)
            scores[i] += turn_points
            display_scores(scores, num_humans)
    
        if scores[i] >= WINNING_SCORE:
            break           

    winner_id = scores.index(max(scores))

    if num_humans == len(scores):
        winner_type = f"Player {winner_id + 1}"
        
    elif is_human(winner_id, num_humans):
        winner_type = "You"
    else:
        winner_type = f"Bot"

    if winner_type == "You":
        print(f"\You win the game with {scores[winner_id]} points!")
    if winner_type == "Bot":
        print(f"\nBot wins the game with {scores[winner_id]} points!")
    else:
        print(f"\n{winner_type} wins the game with {scores[winner_id]} points!")

if __name__ == "__main__":
    main()
