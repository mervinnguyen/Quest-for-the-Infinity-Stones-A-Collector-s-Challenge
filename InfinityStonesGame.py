#infinity stones game

def infinityStonesGame():
    #hashmap representing infinity stones in proper sequence
    infinityStones = {
        1: "Space",
        2: "Reality",
        3: "Power",
        4: "Mind",
        5: "Time",
        6: "Soul"
    }

    print("Welcome to the Infinity Stones Game!")
    print("You are on a quest to collect all the Infinity Stones.")
    print("You will be presented with a series of challenges.")
    print("If you pass the challenge, you will receive an Infinity Stone.")
    print("If you fail the challenge, you will lose an Infinity Stone.")
    print("Your goal is to collect all six Infinity Stones.")
    print("Let's begin!")

    #start the game
    collected = [] #keep track of collected stones
    for order in range(1, 7):
        stone = infinityStones[order]
        while True:
            userInput = input(f"Enter the name of the {order} Infinity Stone: ").strip().capitalize()
            if userInput == stone:
                print(f"Congratulations! You have collected the {stone} Infinity Stone.")
                collected.append(stone)
                break
            else:
                print(f"Sorry, that is incorrect. Try again.")

    #Game complete
    print("Congratulations! You have collected all six Infinity Stones.")
    print(", ".join(collected))
    print("You have successfully completed the Infinity Stones Game!")
    
#run the game
if __name__ == "__main__":
    infinityStonesGame()