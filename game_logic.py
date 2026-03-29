import time
import hint_system

def playGame(scramble, word, difficulty):
    difficultyLevels = {'easy': 5, 'medium': 10, 'hard': 15}

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    score = 0
    maxAttempts = 3
    count = 1
    hasAnswer = False
    total_time = 0
    hintsUsed = 0

    while count <= maxAttempts and hasAnswer == False:
        start_time = time.time()
        userInput = input("Guess the word: ").lower()
        print(f"Attempts remaining: {3-count}.")
        
        hasDigit = False
        for character in userInput:
            if character not in letters:
                hasDigit = True

        if userInput=="hint":
            hint = hint_system.selectHint()
            newScore, newHints = hint_system.useHint(hintsUsed, hint, word, score)
            score = newScore
            hintsUsed = newHints

        elif hasDigit:
            count += 1
            print("Invalid statement")

        elif userInput.lower() == word.lower():
            print(f"You got the word it was {word}!")
            hasAnswer = True
                
        else:
            print("That is the wrong word! Try again!")
            count += 1

    score = score + difficultyLevels[difficulty] * (maxAttempts - count)
    end_time = time.time()
    total_time += (end_time - start_time)
    if hasAnswer:
        print(f"Your score is {score}! You took {count} attempts and {total_time:.2f} seconds!")
    else:
        print(f"You failed to guess the answer in 3 attempts. Your score is {score}. The correct answer is {word}.")


    return score
