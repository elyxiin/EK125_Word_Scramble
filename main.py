# imports
import game_logic 
import scramble

print("Welcome to Guess the Scrambled Word!")
isOn = True

while(True):
    category = scramble.selectCategory()
    difficulty, wordBank = scramble.selectDifficulty(category)
    word, scrambled = scramble.selectWord(wordBank)
    print(f"The scrambled word is {scrambled}")

    score = game_logic.playGame(word, difficulty)

    input("Press enter to play again. \n")