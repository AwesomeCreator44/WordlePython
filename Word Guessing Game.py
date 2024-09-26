import random
exit1 = False

def lengthfunct():
    global length
    global f
    global num
    global length2
    if length == 2:
        f = open("Word2.txt", "r")
        num = random.randint(0, 23)
        length2 = "two"
    elif length == 3:
        f = open("Word3.txt", "r")
        num = random.randint(0, 99)
        length2 = "three"
    elif length == 4:
        f = open("Word4.txt", "r")
        num = random.randint(0, 238)
        length2 = "four"
    elif length == 5:
        f = open("Word5.txt", "r")
        num = random.randint(0, 187)
        length2 = "five"
    elif length == 6:
        f = open("Word6.txt", "r")
        num = random.randint(0, 156)
        length2 = "six"
    elif length == 7:
        f = open("Word7.txt", "r")
        num = random.randint(0, 126)
        length2 = "seven"
    elif length == 8:
        f = open("Word8.txt", "r")
        num = random.randint(0, 75)
        length2 = "eight"
    elif length == 9:
        f = open("Word9.txt", "r")
        num = random.randint(0, 40)
        length2 = "nine"
    elif length == 10:
        f = open("Word10.txt", "r")
        num = random.randint(0, 23)
        length2 = "ten"
    elif length == 11:
        f = open("Word11.txt", "r")
        num = random.randint(0, 9)
        length2 = "eleven"
    elif length == 12:
        f = open("Word12.txt", "r")
        num = random.randint(0, 3)
        length2 = "twelve"
        
while exit1 == False:
    exit2 = 1
    
    length = 0
    while not (2 <= length <= 12):
        length = int(input("Choose a length for each word from 2-12: "))
        difficulty = 0
        while not (difficulty == 1 or difficulty == 2 or difficulty == 3):
            difficulty = int(input("Enter a difficulty. 1 is easy, 2 is moderate, 3 is hard: "))
        
    while exit2 == 1:
        
        lengthfunct()
        possible = f.readlines()
        word = possible[num]
        word = word.rstrip()
        correct = False
        guessCount = 0
        guess = " "
        
        if difficulty == 1:
            while correct == False:
                count = 0
                while len(guess) != length:
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                for i in range(length):
                    if guess[i] == word[i]:
                        count += 1
                if guess == word:
                    print("You have guessed the word!")
                    correct = True
                else:
                    print("Your guess has", count, "letters in common with the word.")
                    guess = ""
                    print(len(word))
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))
            
        if difficulty == 2:
            while correct == False:
                count = 0
                while len(guess) != length:
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                for i in range(length):
                    if guess[i] == word[i]:
                        count += 1
                if guess == word:
                    print("You have guessed the word!")
                    correct = True
                else:
                    print("Your guess has", count, "letters in common with the word.")
                    guess = ""
                    print(len(word))
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))
            
        if difficulty == 3:
            while correct == False:
                count = 0
                while len(guess) != length:
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                for i in range(length):
                    if guess[i] == word[i]:
                        count += 1
                if guess == word:
                    print("You have guessed the word!")
                    correct = True
                else:
                    print("Your guess has", count, "letters in common with the word.")
                    guess = ""
                    print(len(word))
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))

