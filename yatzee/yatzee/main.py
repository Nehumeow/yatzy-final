from player import play_turn
from score import SCORE_SHEET_TEMPLATE, display_score_sheet

def main():
    """Main game logic for Yatzy."""
    print("Welcome to Yatzy!")
    print("=======================================================")

    player1_name = input("Enter the name of the 1st player: ")
    player2_name = input("Enter the name of the 2nd player: ")
    print(
        """
    Rules for Yatzy:

    Basic Sets:
    - **2 PAIRS**: Roll two pairs of matching dice.
    - **3 PAIRS**: Roll three pairs of matching dice.
    - **THREE OF A KIND**: Three dice showing the same value.
    - **FOUR OF A KIND**: Four dice showing the same value.
    - **FIVE OF A KIND**: Five dice showing the same value.

    Straights:
    - **SMALL STRAIGHT**: Five dice showing the values from 1 to 5. Worth 15 points.
    - **BIG STRAIGHT**: Five dice showing the values from 2 to 6. Worth 20 points.
    - **FULL STRAIGHT**: Six dice showing the values from 1 to 6. Worth 21 points.

    Special Combinations:
    - **FULL HOUSE**: A combination of one Pair and one Three of a Kind.
    - **VILLA**: Two Three of a Kinds.
    - **TOWER**: A combination of one Pair and one Four of a Kind.

    Other:
    - **CHANCE**: Score the total of all six dice, regardless of values. Useful as a last resort
      when you have a result that doesn’t fit any other category.
    - **MAXI-YATZY**: All six dice show the same value. Worth 100 points.
    """
    )

    #rules
    
    # Create players with their score sheets and dice
    player1_score_sheet = SCORE_SHEET_TEMPLATE.copy()
    player2_score_sheet = SCORE_SHEET_TEMPLATE.copy()
    player1_dice = [0] * 6
    player2_dice = [0] * 6
    
    # Alternate turns until both players have filled their score sheets
    while None in player1_score_sheet.values() or None in player2_score_sheet.values():
        display_score_sheet(player1_name, player1_score_sheet)
        player1_score_sheet = play_turn(player1_name, player1_score_sheet, player1_dice)
        if None not in player1_score_sheet.values():
            print(f"{player1_name} has completed their score sheet.")
        
        display_score_sheet(player2_name, player2_score_sheet)
        player2_score_sheet = play_turn(player2_name, player2_score_sheet, player2_dice)
        if None not in player2_score_sheet.values():
            print(f"{player2_name} has completed their score sheet.")

    print("\nGame Over!")
    display_score_sheet(player1_name, player1_score_sheet)
    display_score_sheet(player2_name, player2_score_sheet)

    player1_total = sum(score for score in player1_score_sheet.values() if score is not None)
    player2_total = sum(score for score in player2_score_sheet.values() if score is not None)

    print(f"\n{player1_name}'s Total Score: {player1_total}")
    print(f"\n{player2_name}'s Total Score: {player2_total}")

    if player1_total > player2_total:
        print(f"\nCongratulations, {player1_name}! You won!")
    elif player2_total > player1_total:
        print(f"\nCongratulations, {player2_name}! You won!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()
