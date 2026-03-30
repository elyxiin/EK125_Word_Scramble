# EK125 Word Scramble Game

1. You will be given a choice of 5 categries to choose from, please input the number or the category name.
   Inputting an invalid category results in a message telling you to input a valid category.

2. After you will be able to select a difficulty mode, easy, medium, hard. Words with less than 6 characters are easy. Words of length 6-8 are considered medium. Words of length 9 and greater are difficult. 
    Inputting an invalid difficulty will have the user try again.

3. After selecting difficulty, you are given a word thats scrambled. You can either guess the word or type "hint" to reveal the hint pop up menu

4. For hints, you have a first letter hint and a last letter hint, and once you use both of hints there is a message saying there are no more   hints left.

5. Outside of the hint function, you have 3 tries to guess the word, failure to guess the word in 3 tries ends the game and shows your statistics.

6. After the end of each game, you can choose to restart the game.

**Xin's contributions**
- Made a select category function to allow the user to select from 5 categories (animals, foods, countries, science, technology)
- Made a select difficulty function (easy, medium, hard)
- Made a word selection function
- Made a word scrambler function

**Riya's Contributions:**
- Made the function playGame and created a dictionary of if it dictionary and set it equal to the corresponding number
- Create the while loop where it only run if the atempts the user has made is less or equal to three and hasAnswer is False
- Printed the final score and the attempt it took the user and if they didnt get the word it would print the word

**Kiera's Contributions:**
- Made a def select hint system for riya to incorperate into her while loop. 
- Also implemented a counting system for time elapsed while guessing, also rounding the number to two decimal points.
- Set max hints to 2 because there are only two hints, and took away from the score when hiints were used

Future enhancement ideas:
