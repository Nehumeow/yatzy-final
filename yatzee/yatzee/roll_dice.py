import random

def roll_dice(current_dice, keep_indices=None):
    """Roll dice, optionally keeping some dice."""
    if keep_indices is None:
        keep_indices = []
    
    for i in range(6): # change made
        if i + 1 not in keep_indices:  # +1 because user inputs 1-6
            current_dice[i] = random.randint(1, 6)
    return current_dice
