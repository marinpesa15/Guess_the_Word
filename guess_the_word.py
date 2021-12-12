import random

word_lst = ["Python", "JavaScript", "Java", "Brainfuck", "Swift", "Kotlin", "Html", "Bitcoin"]
secretWord = random.choice(word_lst)

print(f"These are the possible choices: {word_lst}")
print("Waiting for the secret Word.../")
print("It's time to guess!")

count = 0
for i in range(len(word_lst)-3):
    guessWord = input("Guess the Word: ")
    if guessWord != secretWord:
        if count == len(word_lst)-(3+1):
            print("You are out of guesses and you haven't guessed the secret Word.")
        else:
            print("Wrong word try again.")
            count += 1
            continue
    elif guessWord == secretWord:
        if count == 0:
            print("You've guessed the Word instantly, Congratulation!")
        elif count == 1:
            print("You've guessed the Word after 1 try, Congratulation!")
        elif count > 1:
            print(f"You've guessed the Word after {count} tries, Congratulation!")
    else:
        break
