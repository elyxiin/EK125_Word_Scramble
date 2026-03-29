import time
import game_logic

def show_word_length(word):
    """reveal the length of the word"""
    length = len(word)
    print("The word has", length, "letters.")

def selectHint():
    hint = 0
    hint_select = input("Please select a hint\n\
        1. First Letter\n\
        2. Last Letter\n\
        3. None (Guess the word)\n")
    if hint_select=='first' or hint_select =='1':
        hint = 'First Letter'
    elif hint_select =='last' or hint_select =='2':
        hint = 'Last Letter'
    elif hint_select == 'none' or hint_select =='3':
        hint = 'None'
    else:
        print(f"{hint_select} is not a valid Hint.")
        return selectHint()
    return hint

def useHint(hintsUsed, hint, word, score):
    maxHints = 2
    if hintsUsed < maxHints:
        print("Hint chosen:", hint)
        if hint == "First Letter":
            score = score - 2
            hintsUsed += 1
            print(f"First letter: {word[0]}, score decreased by 2 points")
        elif hint == "Last Letter":
            score = score - 2
            hintsUsed += 1
            print(f"Last letter: {word[-1]}, score decreased by 2 points")
    else:
        print("Hints are already used up.")

    return score, hintsUsed

