import typing

SCORE_SHEET_TEMPLATE = {
    # Upper section
    'Ones': None, 'Twos': None, 'Threes': None, 
    'Fours': None, 'Fives': None, 'Sixes': None,
    # Lower section
    'One Pair': None, 'Two Pairs': None, 'Three Pairs':None, 'Three of a Kind': None,
    'Villa':None,'Four of a Kind': None, 'Five of a Kind': None, 'Small Straight': None, 'Large Straight': None,
    'Full Straight': None, 'Full House': None, 'Chance': None, 'Yatzy': None
}

NUMBER_CATEGORIES = {
    1: 'Ones', 2: 'Twos', 3: 'Threes', 
    4: 'Fours', 5: 'Fives', 6: 'Sixes'
}

def calculate_possible_scores(dice: list, score_sheet: dict) -> dict:
    """Calculate possible scoring options for the current dice roll."""
    dice_counts = [dice.count(i) for i in range(1, 7)]
    possible_scores = {}

    # Upper section
    for i in range(6):
        category = NUMBER_CATEGORIES[i + 1]
        if dice_counts[i] > 0 and score_sheet[category] is None:
            possible_scores[category] = (i + 1) * dice_counts[i]

    # One Pair
    if score_sheet['One Pair'] is None:
        for i in range(6, 0, -1):
            if dice_counts[i-1] >= 2:
                possible_scores['One Pair'] = i * 2
                break

    # Two Pairs
    if score_sheet['Two Pairs'] is None:
        pairs = []
        for i in range(6, 0, -1):
            if dice_counts[i-1] >= 2:
                pairs.append(i)
            if len(pairs) == 2:
                possible_scores['Two Pairs'] = sum(pairs) * 2
                break

    # Three pairs
    if score_sheet['Three Pairs'] is None:
        pairs = []
        for i in range(6, 0, -1):
            if dice_counts[i - 1] >= 2:
                pairs.append(i)
            if len(pairs) == 3:
                possible_scores['Three Pairs'] = sum(pairs) * 2
                break


    # Three of a Kind
    if score_sheet['Three of a Kind'] is None:
        for i in range(6, 0, -1):
            if dice_counts[i-1] >= 3:
                possible_scores['Three of a Kind'] = i * 3
                break

    # Villa
    if score_sheet['Villa'] is None:
        # filter dice_counts where 3
        pairs = []
        for i in dice_counts:
            if i == 3:
                pairs.append(i)
        if len(pairs) >=2:
            possible_scores['Villa'] = sum(dice)





    # Four of a Kind
    if score_sheet['Four of a Kind'] is None:
        for i in range(6, 0, -1):
            if dice_counts[i-1] >= 4:
                possible_scores['Four of a Kind'] = i * 4
                break


     # Five of a Kind
    if score_sheet['Four of a Kind'] is None:
        for i in range(6, 0, -1):
            if dice_counts[i-1] >= 5:
                possible_scores['Five of a Kind'] = i * 5
                break



    # Small Straight
    if score_sheet['Small Straight'] is None:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            possible_scores['Small Straight'] = 15

    # Large Straight
    if score_sheet['Large Straight'] is None:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            possible_scores['Large Straight'] = 20

    # Full straight
    if score_sheet['Full Straight'] is None:
        if sorted(dice) == [1, 2, 3, 4, 5, 6]:
            possible_scores['Full Straight'] = 21

    # Full House
    if score_sheet['Full House'] is None:
        sorted_counts = sorted(dice_counts, reverse=True)
        if sorted_counts[0] == 3 and sorted_counts[1] == 2:
            res = sorted(dice)
            res.pop(0)
            possible_scores['Full House'] = sum(res)


    # Chance
    if score_sheet['Chance'] is None:
        possible_scores['Chance'] = sum(dice)

    # Yatzy
    if score_sheet['Yatzy'] is None:
        if 6 in dice_counts:
            possible_scores['Yatzy'] = 100

    return possible_scores

def display_score_sheet(player_name: str, score_sheet: dict):
    """Display the current player's score sheet."""
    print(f"\n{player_name}'s Score Sheet:")

    # Upper Section
    print("\nUpper Section:")
    upper_categories = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    upper_section_total = 0

    print("{:<15} {:<10}".format("Category", "Score"))
    print("-" * 25)
    for category in upper_categories:
        score = score_sheet[category]
        print("{:<15} {:<10}".format(category, score if score is not None else '-'))
        if score is not None:
            upper_section_total += score

    # Calculate bonus
    bonus = 50 if upper_section_total >= 63 else 0

    print("-" * 25)
    print("{:<15} {:<10}".format("Upper Total", upper_section_total))
    print("{:<15} {:<10}".format("Bonus", bonus))

    # Lower Section
    print("\nLower Section:")
    total_score = upper_section_total + bonus
    lower_categories = ['One Pair', 'Two Pairs', 'Three Pairs', 'Three of a Kind','Villa', 'Four of a Kind',
                        'Small Straight', 'Large Straight', 'Full House', 'Chance', 'Yatzy']

    print("{:<15} {:<10}".format("Category", "Score"))
    print("-" * 25)
    for category in lower_categories:
        score = score_sheet[category]
        print("{:<15} {:<10}".format(category, score if score is not None else '-'))
        if score is not None:
            total_score += score

    print("-" * 25)
    print(f"\nTotal Score: {total_score}")
