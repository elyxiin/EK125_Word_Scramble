
maxAttempts = 3
    count = 1
    hasAnswer = False

def selectHint():
    hint = 0
    hint_select = input("Please select a hint\n\
        1. First Letter\n\
        2. Last Letter\n\
        3. None (Guess the word)\n")

    if hint_select=='' or hint_select =='1':
        hint = 'First Letter'
    elif hint_select =='' or hint_select =='2':
        hint = ('Last Letter')
    elif hint_select == 'None' or hint_select =='3':
        hint = 'None'
    else:
        print(f"{hint_select} is not a valid Hint.")
        selectHint()
    return hint


score = 1000
#def show_word_length(word):
   # """reveal the length of the word"""
    #length = len(word)
    #print("The word has", length, "letters.")


hint = selectHint()
print("Hint chosen:", hint)
if hint == "First Letter":
    score = score-2
    print("First letter:", word[0])
elif hint == "Last Letter":
    score = score-2
    print("Last letter:", word[-1])
