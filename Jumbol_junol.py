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

print("~" * 40)
print()
print("   Welcome to Jargon Jumble!")
print("   A Tech-Themed Word Scramble Game")
print()
print("~" * 40)


word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
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

print(f"Your final score is {score}/5")
print(" A message for you -->")
print()
if score == 5:
    print("Flawless! All tests passing, zero bugs.")
elif score == 4:
    print("Near perfect, only one failing test!")
elif score == 3:
    print("Good effort! The code runs, and that's what counts.")
else:
    print("Have you tried turning it off and on again?")








#print(used)











