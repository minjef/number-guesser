import random

def main():
#Intro
    print("The aim of the game is to guess the right number in as few guesses as posible")

#Asks if user wants to play
    answer = input("Are you ready to play? ")
    if answer.lower() != "yes":
        print("Goodbye")
        quit()
    print("Great let's play!")

#Asks for a number and checks if it's a number and if it's higher than 0. Converts input to int
    top_of_range = input("Type a number to select your range you want to play in: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please type a number larger than 0 next time")
            print("Goodbye")
            quit()
    else:
        print("Please type a number next time")
        print("Goodbye")
        quit()

#Light banter for the users selection  
    if top_of_range <=5:
         print(f"{top_of_range} huh? Playing on easy mode i see, oh well...")
    if top_of_range > 5 and top_of_range <= 10:
         print(f"I see you'd like a quick game with a {top_of_range}")
    if top_of_range > 10 and top_of_range <= 15:
         print(f"{top_of_range}? This might get a bit chalanging")
    if top_of_range > 15 and top_of_range <= 20:
         print(f"It might be bit hard with a {top_of_range}")
    if top_of_range > 20 and top_of_range <= 50:
         print(f"{top_of_range}: Hard mode activated")
    if top_of_range > 50:
         print(f"Wow a {top_of_range}! You're a masochist, i like it!")

#Generates a random number from 0 to user selected number
    random_num = random.randint(0, top_of_range)
    
#Asks to make a guess, compares it to the generated random number, counts guesses
    guesses = 0
    while True:
        guesses += 1
        user_guess = input("Make a guess: ")

        #checks if the guess is a number
        if user_guess.isdigit:
            user_guess = int(user_guess)
        else:
            print("Please type a number next time")
            continue
        
        #compares the guess to the random number, makes suggestions if its above or bellow
        if user_guess == random_num:
            print("Nice, You got it!")
            break
        
        elif user_guess > random_num:
                print("Your guess was above the number")
        else:
                print("Your guess was bellow the number")
    
    print(f"You got it right in {guesses} guesses")

main()