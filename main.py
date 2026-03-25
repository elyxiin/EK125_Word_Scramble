# imports
import csv
import random

# reading data from 'word_bank'
with open('word_bank.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)

    # categories
    categories = {
        'animal' : [],
        'food' : [],
        'country' : [],
        'science' : [],
        'technology' : [] 
        }

    for row in reader:
        for key in categories:
            if row[key]: # since some categories have more values than others, checks to see if it is empty
                categories[key].append(row[key])

def selectCategory():
    """Allows user to select category either by typing in the category or corresponding number"""
    category = 0

    # category menu
    user = input("Please select a category\n\
                 1. Animals \n\
                 2. Foods \n\
                 3. Countries \n\
                 4. Science \n\
                 5. Technology\n").lower()
    
    if user=='animals' or user=='1':
        category = 'animal'
    elif user=='foods' or user=='2':
        category = 'food'
    elif user=='countries' or user=='3':
        category = 'country'
    elif user=='science' or user=='4':
        category = 'science'
    elif user=='technology' or user=='5':
        category = 'technology'
    else:
        print(f"{user} is not a valid category.")
        selectCategory()
    return category
    
def selectDifficulty(category):
    """Returns player selected difficulty and a refined word bank only including words of the selected difficulty within the selected category."""
    difficulty = ''
    wordBank = None
    user = input("Please select a difficulty: \n" \
    "1. Easy \n" \
    "2. Medium \n" \
    "3. Hard \n").lower()

    if user == 'easy' or user=='1':
        difficulty='easy'
        wordBank = [word for word in categories[category] if len(word)<6]
    elif user == 'medium' or user=='2':
        difficulty='medium'
        wordBank = [word for word in categories[category] if 5<len(word) and len(word)<9]
    elif user == 'hard' or user=='3':
        difficulty='hard'
        wordBank = [word for word in categories[category] if 8<len(word)]
    else:
        print(f"\n{user} is not a valid difficulty.")
        selectDifficulty(category)
    
    return difficulty, wordBank

def scramble(word):
    lstWord = list(word)
    chars = []

    # Works by selecting a random index and removing that letter from the pool until there's no letters left in the original and they have all been added to the new
    for i in range(len(word)):
        rand = random.randint(0,len(lstWord)-1) # random index integer
        chars.append(lstWord.pop(rand))
    scrambled = "".join(chars) # joins the list into a string
    
    # check to make sure the word is scrambled
    if scrambled == word:
        scramble(word)

    return scrambled

def selectWord(wordBank):
    """Selects a scrambled word from the word bank."""
    rand = random.randint(0,len(wordBank)-1)
    word = wordBank[rand]
    scrambled = scramble(word)
    return word, scrambled



print("Welcome to Guess the Scrambled Word!")
isOn = True

while(True):
    category = selectCategory()
    difficulty, wordBank = selectDifficulty(category)
    word, scrambled = selectWord(wordBank)

    difficultyLevels = {'easy': 5, 'medium': 10, 'hard': 15}

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    score = 0
    maxAttempts = 3
    count = 0

    print(f"The scrambled word is {scrambled}")
    while count < maxAttempts:
        userInput = input("Choose a word: ").lower()

        for character in userInput:

            if character not in letters:
                print("Invalid statement")
                count += 1

            if userInput.lower() == word.lower():
                print(f"You got the word it was {word}!")
                break
            
            else:
                print("That is the wrong word! Try again!")
                count += 1

    score = difficultyLevels[difficulty] * (maxAttempts - count)
    print(f"Your score is {score}! You took {count} attempts!")

    print(word[-1])

    input("Press enter to play again. ")

