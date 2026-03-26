# Development Log

## Xin
**03.23.2026**
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

## Riya

## Kiera