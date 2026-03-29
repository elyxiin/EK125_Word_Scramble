
import time

maxHints = 2
hintsUsed = 0
score = 0
maxAttempts = 3
count = 1
hasAnswer = False
total_time = 0

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

show_word_length(word)
score = 0

while count <= maxAttempts and not hasAnswer:
    # Record time before guess
    start_time = time.time()
    userInput = input(f"Attempt {count}: Choose a word: ").lower()
    # Record time after guess
    end_time = time.time()

    # Accumulate the time spent on this specific guess
    total_time += (end_time - start_time)

while hintsUsed < maxHints:
    hint = selectHint()
    print("Hint chosen:", hint)
    if hint == "First Letter":
        score = score-2
        hintsUsed += 1
        print("First letter:", word[0])
    elif hint == "Last Letter":
        score = score-2
        hintsUsed += 1
        print("Last letter:", word[-1])
    elif hint == "None":
        userInput = input("Choose a word: ").lower()

