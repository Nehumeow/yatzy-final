from roll_dice import roll_dice
from score import calculate_possible_scores, display_score_sheet

def play_turn(player_name: str, score_sheet: dict, dice: list) -> dict:
    """Play a single turn for a player."""
    print(f"\n{player_name}'s turn!")
    rolls_left = 3
    while rolls_left > 0:
        print(f"\nRolling dice...")
        if rolls_left == 3:
            roll_dice(dice)
        print(f"Roll #{4-rolls_left}: {dice}")
        
        if rolls_left > 1:
            while True:
                try:
                    keep_input = input("Enter the indexes (1-5) of the dice you want to keep, separated by spaces\n"
                                       "(or press enter to re-roll all): ").strip()
                    if not keep_input:
                        roll_dice(dice)
                        break
                    
                    keep_indices = [int(x) for x in keep_input.split()]
                    if all(1 <= x <= 6 for x in keep_indices): # change made
                        roll_dice(dice, keep_indices)
                        break
                    else:
                        print("Please enter numbers between 1 and 5.")
                except ValueError:
                    print("Please enter valid numbers separated by spaces.")
        
        rolls_left -= 1

    print(f"Final dice: {dice}")
    
    possible_scores = calculate_possible_scores(dice, score_sheet)
    if not possible_scores:
        print("No possible scoring categories left. You must cross out a category.")
        display_score_sheet(player_name, score_sheet)
        while True:
            category = input("Enter category to cross out: ")
            if category in score_sheet and score_sheet[category] is None:
                score_sheet[category] = 0
                print(f"Crossed out {category} for 0 points.")
                break
            print("Invalid category. Try again.")
    else:
        print("\nPossible categories for this roll:")
        options = list(possible_scores.items())
        for i, (category, score) in enumerate(options, 1):
            print(f"{i}. {category} ({score} points)")
        
        while True:
            choice = input("Choose a category by number: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(options):
                    category, score = options[index]
                    score_sheet[category] = score
                    print(f"Scored {score} points in {category}")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number.")
    
    return score_sheet
