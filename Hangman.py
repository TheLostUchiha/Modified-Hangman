# Modified-Hangman
import random
words = ["ability", "absence", "accused", "adviser", "alcohol", "alleged", "anybody", "arrange", "assault", "attract",
         "barrier", "battery", "believe", "besides", "billion", "cabinet", "capital", "century", "chapter", "crystal",
         "deficit", "develop", "disease", "eastern", "element", "examine", "express", "factory", "failure", "feature",
         "forever", "gallery", "genuine", "hanging", "heavily", "himself", "imagine", "install", "involve", "journey",
         "killing", "learned", "liberal", "loyalty", "maximum", "million", "minimum", "monthly", "notable", "offense",
         "optical", "outlook", "pacific", "pattern", "perfect", "radical", "receipt", "regular", "science", "service",
         "several", "telling", "trouble", "tonight", "uniform", "upgrade", "utility", "vehicle", "visible", "visible",
         "waiting", "warrant", "willing"]

theWord = words[random.randint(0, len(words)-1)]

print("Welcome to HANGMAN")
print("You have to guess the given word in this game, letter by  letter.")
print("every wrong guess of a letter will cost you 1 life and you have 3 lives in total.")
print("If you exhaust all your lives before completing the word, then...")
print("Game Over!")

lives = 3
unright = 0
rnge = [0, 1, 2, 3, 4, 5, 6]
word = ["_", "_", "_", "_", "_", "_", "_"]

for i in range(0, 3):
    num = random.choice(rnge)
    word[num] = theWord[num]
    rnge.remove(num)


def compileword(w1):
    w2 = ""
    for j in range(0, len(w1)):
        w2 += w1[j]
    return w2


wrd1 = compileword(word)

print("Here is the word: " + wrd1 + "\n")

while lives > 0 or unright == 4:
    guess = input("Enter the letter you have guessed: ").lower()
    ntimes = 0
    right = 0
    for x in range(0, 6):
        if guess == theWord[x] and wrd1[x] != theWord[x]:
            word[ntimes] = guess
            right += 1
            unright += 1
            break
        else:
            ntimes += 1
    if right == 0:
        lives -= 1
        print("Wrong guess, you lost 1 life.")
        print(f"Lives left: {lives}\n")
        print(f"{compileword(word)}\n")
    elif right == 1:
        print("Good guess.\n")
        print(f"{compileword(word)}\n")
    if unright == 4:
        print("You have guessed all characters correctly")
        print("Congratulations")
        print("GAME OVER")
        break
if lives == 0:
    print("You're out of lives.")
    print(f"The correct word was:   {theWord}")
    print("Game over")
