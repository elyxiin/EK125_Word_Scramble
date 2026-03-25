def playGame(scramble, word, difficulty):
    difficultyLevels = {'easy': 5, 'medium': 10, 'hard': 15}

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    score = 0
    maxAttempts = 3
    count = 1
    hasAnswer = False

    while count < maxAttempts and hasAnswer == False:
        userInput = input("Choose a word: ").lower()
        
        hasDigit = False
        for character in userInput:
            if character not in letters:
                hasDigit = True

        if hasDigit:
            count += 1
            print("Invalid statement")

        elif userInput.lower() == word.lower():
            print(f"You got the word it was {word}!")
            hasAnswer = True
                
        else:
            print("That is the wrong word! Try again!")
            count += 1

    score = difficultyLevels[difficulty] * (maxAttempts - count)
    print(f"Your score is {score}! You took {count} attempts!")

    return score
