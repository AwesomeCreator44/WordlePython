import random #random module for random words
exit1 = False #main code loop setup 1

def lengthfunct(): #function for deciding length
    global length
    global f
    global num
    global length2
    if length == 2: #checks length
        f = open("Word2.txt", "r") #opens list of words
        num = random.randint(0, 23) #picks random number to decide random word
        length2 = "two" #turns number length into words
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
        
while exit1 == False: #main code loop setup 2
    exit2 = 1 #game loop setup 1
    
    length = 0
    while not (2 <= length <= 12): #ensuring that user picks number in range
        length = int(input("Choose a length for each word from 2-12: ")) #allows user to pick length of words
        difficulty = -1
        while not ( 0 <= difficulty <= 3): #ensuring that user picks number in range
            difficulty = int(input("Enter a difficulty. 1 is normal, 2 is difficult, 3 is impossible (0 for more info): ")) #allows user to pick difficulty level

    if difficulty == 0:
        print("\nINFO \n\nDifficulty 1 - Normal \nVery similar to the real Wordle \n\nDifficulty 2 - Moderate \nYou are given two counts - letters in the word letters in the correct position \n\nDifficulty 3 - Impossible \nYou are only given one count, with the number of letters in the correct position \n")
        exit2 = 2

    while exit2 == 1: #game loop setup 2
        
        lengthfunct() #calls the function for deciding length
        possible = f.readlines() #puts all possible words into a variable
        word = possible[num] #picks random word from possible word list using the random number decided earlier
        word = word.rstrip() #removes the extra space at the end of each word
        correct = False #game loop setup 3
        guessCount = 0 #ensures guess count is 0 at beginning
        guess = "" #defines the guess variable
        attempts = 1 #defines attempts variable


                
        if difficulty == 1: #tells user exactly which letters are correct, in the correct place, or incorrect entirely
            while correct == False:
    
                while len(guess) != length: #ensures the user enters a guess of the correct length
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                    print("")

                for i in range(length): #creates loop to check each letter
                    if guess[i] == word[i]: 
                        print("The letter", guess[i], "is in its correct position") #checks for words in the correct position
                    elif guess[i] in word: 
                        print("The letter", guess[i], "is in the word but is in the wrong position") #checks for letters in the word which are in the wrong position 
                    else:
                        print("The letter", guess[i], "is not in the word") #checks for letters which aren't in the word
                print("")
                    
                if guess == word:
                    if attempts == 1:
                        print("You have guessed the word! It only took one attempt!")
                    else:
                        print("You have guessed the word! It only took", attempts, "attempts.")
                    correct = True
            
                else:
                    guess = ""
                    attempts += 1
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))


            
        elif difficulty == 2: #includes two counts - one for letters in the right place and one for letters in the wrong place
            while correct == False:
                
                count = 0
                count2 = 0
                
                while len(guess) != length:
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                    
                for i in range(length):
                    if guess[i] == word[i]:
                        count += 1
                    if guess[i] in word: #loop to see how many letters in the guess are in the real word in total
                        count2 += 1
                        
                if guess == word:
                    if attempts == 1:
                        print("You have guessed the word! It only took one attempt!")
                    else:
                        print("You have guessed the word! It only took", attempts, "attempts.")
                    correct = True
                    
                else:
                    print("Your guess has", count2, "letter(s) in common with the word, with", count, "in the correct position.")
                    guess = ""
                    attempts += 1
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))


            
        elif difficulty == 3: #checks game difficulty
            while correct == False: #game loop setup 4
                count = 0 #defines count used for each letter
                while len(guess) != length: #ensures the user enters a guess of the correct length
                    print("Enter a", length2, "letter word: ")
                    guess = input("")
                for i in range(length): #creates loop to check each letter
                    if guess[i] == word[i]: #checks guess letters with random word letters
                        count += 1 #adds to count to see number of letters in common
                if guess == word:
                    if attempts == 1:
                        print("You have guessed the word! It only took one attempt!")
                    else:
                        print("You have guessed the word! It only took", attempts, "attempts.")
                    correct = True #breaks loop
                else:
                    print("Your guess has", count, "letter(s) in the correct position.")
                    guess = ""
                    attempts += 1
            exit2 = int(input("Type 1 to get a new word or 2 to exit to menu: "))
