import random

#words = ["cloud" , "cleats" , "shinguards"]

#word = random.choice(words)
#print(word)

#letters = list(word)
#print(letters)

#random.shuffle(letters)
#print(letters)

#scrambled_word = "".join(letters)
#print(f"Scrambled word is : {scrambled_word}")

print("-" * 60)
print()
print()
print("  Welcome to Jumbol Junol!")
print("  A Fun Word Scramble Game")
print()
print()
print("-" * 60)


word_bank = [
    
]

player_start = input("Do you want to play the game ? (type 'quit' if not)")

TOTAL_ROUNDS = 5
start_round = 1 

score = 0

while start_round <= TOTAL_ROUNDS:
    
    if player_start == "quit":
        print("Thanks for playing the game !")
        break
        
    print()
    print(f"NOW PLAYING ROUND {start_round}")
    print()
    start_round += 1
    response = input("Type 'skip' to skip the round or type start to start... ")
    cleaned_response = response.strip().lower()


    word , hint = random.choice(word_bank)
    used = []
    while (word , hint) in used:
        word , hint = random.choice(word_bank)

    used.append((word , hint))



    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)
    caps_scrambled = scrambled_word.upper()



    if cleaned_response == "skip":
        print(f"Skipped ! ,the word was {word}")
        print()
    else:
    
        print(f"Scrambled: {caps_scrambled}")
        print()
        word_guess = input("What is the word (to ask for a hint type 'hint') ? ")

        if word_guess == "hint":
            print(f"The hint is : {hint}")
            print()
            word_guess = (input("What is the word? ")).strip().lower()
            
    
        if word == word_guess: 
            print("Your guess is correct ! ")
            score += 1 
        elif word != word_guess:
            print(f"Sorry the word was {word}")
print()
print()

print(f"Your final score is {score}/{TOTAL_ROUNDS}")
print(" A message for you -->")
print()
if score == 5:
    print("Victory!!! You beat this game ! ")
elif score == 4:
    print("Just one away from victory!")
elif score == 3:
    print("Nice try !")
else:
    print("Maybe try again to beat the game ? :)")








#print(used)











