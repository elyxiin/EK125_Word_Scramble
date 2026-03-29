# Development Log

## Xin
**03.23.2026**
Time: 1.5 hours
* imported CSV module and CSV file
> I chose to use a CSV value to organize the data separately from the main file. It reduces clutter in the main file. I imported the CSV module to better work with the data.

> Originally, I accidentally split the data into rows instead of columns.

```with open('word_bank.csv',newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    headings = next(reader) # separates headers
    data = []

    for row in reader:
        data.append(row[:]) 
```

> I adjusted the code so each column would now be its own list. However, it the code was unnecessarily long. I knew I could make it more condensed and cleaner.

```with open('word_bank.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    headings = next(reader) 

    # categories
    animal = []
    food = []
    country = []
    science = []
    technology = []

    for row in reader:
        if row['animal']!='':
            animal.append(row['animal'])
        if row['food']!='':
            food.append(row['food'])
        if row['country']!='':
            country.append(row['country'])
        if row['science']!='':
            science.append(row['science'])
        if row['technology']!='':
            technology.append(row['technology'])
```

> Made the code more concise and clean by utilizing for loops. Categories are now kept in a dictionary.
```
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
```

* added selectCategory() function
> Allows user to select a category.

> Originally, the categories were going to be assigned by number. 
```if user=='animals' or user=='1':
        category = 1
    elif user=='foods' or user=='2':
        category = 2
    elif user=='countries' or user=='3':
        category = 3
    elif user=='science' or user=='4':
        category = 4
    elif user=='technology' or user=='5':
        category = 5
    else:
        print("{user} is not a valid category.")
        selectCategory()
    return category
```
>However, I realized it would be more convenient to have them stored as strings instead. Therefore, they could be used as keys for direct indexing as well as in print statements to label the category.

```if user=='animals' or user=='1':
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
```
* added selectDifficulty() function
> Allows user to select difficulty.
* added scramble() function
> scrambles the word passed through the function
* added selectWord() function
> the function selects a word and runs that word through the scrambler
* left a temporary testing portion in the code as reference
> As I wrapped up most of my part thus far, I left a showcase portion at the bottom of the main file. As the next modules build off of the work I completed, it serves as a reference to the utilization of my functions. Later, as the project progresses, this snippet will be removed.

```
print("\nTesting")

category = selectCategory()
difficulty, wordBank = selectDifficulty(category)
word, scrambled = selectWord(wordBank)

print(f"Category: {category}")
print(f"Difficulty: {difficulty}")
print(f"\nFull word bank: {categories[category]}")
print(f"\nRefined word bank: {wordBank}")
print(f"\nSelected word: {word}")
print(f"Scrambled word: {scrambled}")
```

**03.25.2026**
Time: 20 minutes
Time so far: 1 hour and 50 minutes
* Removed testing statements
* Added a welcoming statement into the game as well as a game loop to allow continuous replays
```
print("Welcome to Guess the Scrambled Word!")
isOn = True

while(True):
```

**03.26.2026**
Time: 5 minutes
Time so far: 1 hour and 55 minutes
* Moved all my functions into a separate file scramble.py to reduce clutter in main

**03.29.2026**
- Worked on merging everyone's part together.
- Took part in a lot of debugging. Besides myself, my team members did not have any prior experience with github so they were having troubles getting the code to work seamlessly together. Together, we worked on ironing out the details. 


## Riya

## Kiera
Student Name: Kiera Rampersad
Game Title: Word Scramble
My Module: C

SESSION #: _1__
Date: 3/25/26
Time spent this session: 1.5 hours
Total time so far: 1.5 hours

WHAT I WORKED ON TODAY:
Setting up defining variables like revealing the first letter even though I have not done the score system fully
I made a menu for the users to pick what type of hint they want to use and I will later try to loop it so that it pops up if they haven’t guessed the word yet

CHALLENGE I HIT:
Trying to configure the hint menu was confusing at first, I realized I didn’t need my def functions for the hints
My syntax for the menu pop up was wrong and I got an error
"hint_select = input("Please select a hint\n\
                     ^
Syntax Error: unterminated string literal (detected at line 121))

I also messed up by using a lower case l in “letter” while the rest of them were Uppercase so the hint was not printing properly

HOW I FIGURED IT OUT:
I looked over my code and found I was missing a quotation mark at the end of the string.
I asked my teammate to look over my code for bugs and she also could not find it
I ended up finding the lowercase l and fixed it
I also just added if statements after my def function for choosing a hint instead of more def functions because I don’t know why I did that

CODE BEFORE (if you fixed something):
```
hint = input("Please select a category\n\
        1. First Letter\n\
        2. Last Letter\n\
        2. Word Length\n\
        4. None (Guess the word)\n\
             
score = 1000
def show_word_length(word):
    """reveal the length of the word"""
    length = len(word)
    print("The word has", length, "letters.")

def reveal_first_letter(word, score):
    """reveal the first letter from the word"""
    score -= 2
    print("Hint: The first letter is", word[0])
    return score

def reveal_last_letter(word, score):
    """reveals the last letter from the word"""
    score -= 2
    print("Hint: The last letter is", word[-1])
    return score

```

CODE AFTER:

```
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
```

WHAT I LEARNED:
I learned that not everything needs to be in a def function, and I should start my code from the order it runs instead of jumping around
I learned how to effectively debug my code with minor mistakes

WHAT'S NEXT:
Next I need the point system to print on the screen
I also need to make the word length section
Make sure the Hint menu keeps looping until the user guesses the word

**SESSION #: 2**

Date: 3/26/26

Time spent this session: 1 hours

Total time so far: 2.5 hours

WHAT I WORKED ON TODAY:
I made a while function for the hints system so that while the hints was less than the max hints available it would loop.
I also printed the word length

CHALLENGE I HIT:
I forgot to set a value for the counting hints so it gave me an error that there was no variable to refer too
I also needed to set a maxHints function

HOW I FIGURED IT OUT:
I just fixed it and added it
CODE BEFORE (if you fixed something):

```
while hintsUsed =! 0
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
```
CODE AFTER:
```
maxHints = 2
hintsUsed = 0
show_word_length(word)
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
# paste the working version here
```

WHAT I LEARNED:
I learned to always check if there is set variable to 0 before trying to add more to it

WHAT'S NEXT:
I am worried about the time counting function because I have never used it before, so I might need help from someone


SESSION #: 3
Date: 3/29/26
Time spent this session: .5 hours
Total time so far: 3 hours


WHAT I WORKED ON TODAY:
- inserting time function to the loop that tracks how many guessing attempts you have made
- also figuring out where is the best place to put it
- changing variable names to match eachothers so the final code can run smoothly.
- implemented the function into the rest of the code

CHALLENGE I HIT:
- I put the end time function in the loop, so it was resetting the end time everytime there was another guess
- I didn't get an error, but the time printed at the end did not represent the actual time it tok in total.



HOW I FIGURED IT OUT:
- my teammate looked over my code and suggested I put the end time function outside of the loop, 
because it would need to stay counting for each guess
- also I forgot to add a round function


CODE BEFORE (if you fixed something):

```
# while count <= maxAttempts and not hasAnswer:
    # Record time before guess
    start_time = time.time()
    userInput = input(f"Attempt {count}: Choose a word: ").lower()
    # Record time after guess
    end_time = time.time()

    # Accumulate the time spent on this specific guess
    total_time += (end_time - start_time)
```

CODE AFTER:

```
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
```

WHAT I LEARNED:


(What do you understand better now? What would you do differently next time?)


WHAT'S NEXT:
(What do you still need to do? What are you worried about?)


QUESTIONS FOR TEAM/INSTRUCTOR:


(Anything you're still confused about?)

