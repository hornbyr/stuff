# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)


prompt = " Please enter your bet: "
prompt2 = "\n Please press enter to continue our type quit "
i = 0
k = 0
bankroll = 20
print("\n Bank Roll = " + str(bankroll))
print(" ANTE = $5 ")

while True:
    # Print first 2 cards and make bet
    i= i +1
    print("\n  1st card is:", deck[i][0], "of", deck[i][1])
    card1 = deck[i][0]
    i= i+ 1
    print("  2nd card is:", deck[i][0], "of", deck[i][1])
    card2 = deck[i][0]

    # Take Bet
    bet = input(prompt)
    if bet == "quit":
        print(" Game Over.  You quit.")
        break
    else:
        intbet = int(bet) + 5

    # Show 3rd card
    i = i + 1
    print("  3rd card is: ", deck[i][0], "of", deck[i][1])
    card3 = deck[i][0]

    # compute win or loss
    if ((card3 < card1) and (card3 > card2)) or ((card3 > card1) and (card3 < card2)):
        bankroll = bankroll + intbet
        print(" >You win $" + str(intbet) + " -> Your new bank roll = $" + str(bankroll))
    elif ((card3 == card1) or (card3 == card2)):
        bankroll = bankroll - (2 * intbet)
        print(" >You Lose double $" + str(intbet*2) + " -> Your new bank roll = $" + str(bankroll))
    else:
        bankroll = bankroll - intbet
        print(" >You Lose $" + str(intbet) + " -> Your new bank roll = $" + str(bankroll))

    if bankroll > 100:
        print (" Game Over.  You win!")
        print(" Bank Roll = " + str(bankroll))
        break
    pause = input(prompt2)
    if (pause == "quit"):
        print(" Bank Roll = " + str(bankroll))
        break

    # Reshuffle at 51
    if i > 50:
        random.shuffle(deck)
        i = 0