import random

#scoring function - score everthing by value (face cards are worth 10)
#Then score the aces. If making the ace 10 would make you bust, then don't do that
#arguments: hand (list of cards. [[number, suit]])
#returns: the score of that hand
def score(hand):
    score=0
    #score everything except the aces
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            score+=10
        elif card[0]=='A':
            pass
        else:
            score+=int(card[0])
    #score the aces
    for card in hand:
        if card[0]=="A":
            if score+11>21:
                score+=1
            else:
                score+=11
    return score

#shuffling: shuffles the list
#arguments: card_deck: list
#returns: shuffled cards
def shuffling(card_deck):
    for i in range(1000):
        elem1=random.randrange(len(card_deck))
        elem2=random.randrange(len(card_deck))
        holder=card_deck[elem1]
        card_deck[elem1]=card_deck[elem2]
        card_deck[elem2]=holder
    return card_deck
#Potential bug? since it had the -1 originally after (card_deck), it would then not count the last card (which would be king of whatever suit)

#dealing: deals cards to player's list, which can be used for hitting
#arguments: player_hand: list, card_deck: list, gonebust: playerhand, win: player_hand, dealer_hand
#returns: cards to player's hand, list with new cards
def dealing(playerhand, carddeck, quanvalue):
    for i in range(quanvalue):
        playerhand.append(carddeck.pop(0))
    return None
    
#gonebust: checks if the player has gone bust
#arguments: playerhand: list
#returns: boolean to check if player has gone bust or not
def gonebust(playerhand):
    if score(playerhand) > 21:
        return True
    else:
        return False
        
#win: checks who actully wins the game
#arguments: player_hand: list, dealer_hand: list)
#returns: boolean to check who won the game
def win(player_hand, dealer_hand):
    if gonebust(player_hand) == False and gonebust(dealer_hand):
        return True
    elif gonebust(player_hand):
        return False
    elif score(player_hand) <= score(dealer_hand):
        return False
    else:
        return True

#card_deck is a list of the cards in a deck
#Each card is represented by a list of the form [number, suit]
#e.g. the 2 of spades is [2, S] and the Jack of Hearts is [J, H]
#To keep things consistent, both number and suit are strings
card_deck=[
["A", "H"],["2", "H"],["3", "H"],["4", "H"],["5", "H"],["6", "H"],["7", "H"],["8", "H"],["9", "H"],["10", "H"],["J", "H"],["Q", "H"],["K", "H"],
["A", "D"],["2", "D"],["3", "D"],["4", "D"],["5", "D"],["6", "D"],["7", "D"],["8", "D"],["9", "D"],["10", "D"],["J", "D"],["Q", "D"],["K", "D"],
["A", "S"],["2", "S"],["3", "S"],["4", "S"],["5", "S"],["6", "S"],["7", "S"],["8", "S"],["9", "S"],["10", "S"],["J", "S"],["Q", "S"],["K", "S"],
["A", "C"],["2", "C"],["3", "C"],["4", "C"],["5", "C"],["6", "C"],["7", "C"],["8", "C"],["9", "C"],["10", "C"],["J", "C"],["Q", "C"],["K", "C"],
]

#Also available as a tuple for when we reset
card_deck_master=tuple(card_deck)

#initial hands
player_hand=[]
dealer_hand=[]

#initialize scores:
player_score=0
dealer_score=0
num_games=0
num_wins=0

#hit, bust, keep playing
hit='y'
bust=False
keep_playing='y'

while keep_playing=='y':
    #reset, and display the player's and dealer's hands
    card_deck=list(card_deck_master)
    player_hand=[]
    dealer_hand=[]
    shuffling(card_deck)

    #deal two cards to the player and display them (may output just the list with no formatting)
    dealing(player_hand,card_deck, 2)

    print "Player hand: " + str(player_hand)

    #score player's hand 
    player_score=score(player_hand)

    #ask if they want to hit. If they bust, they lose.
    hit=raw_input("Would you like to hit? (y/n) ")
    while hit=='y' and bust==False:
        player_hand.append(card_deck.pop(0))
        player_score=score(player_hand)

        if player_score>21:
            bust=True
        else:
            print "Player hand: ", player_hand
            hit=raw_input("Would you like to hit again? (y/n) ")

    print "Your score: ", player_score

    #if the player hasn't bust, keep on dealing cards to the dealer until their score is >17. Don't display the hand until the end.
    for i in range(2):
        dealer_hand.append(card_deck.pop(0))

    dealer_score=score(dealer_hand)
	
    #This checks if the player has been busted or not.
    if gonebust(player_hand) == False:
        while dealer_score<=17:
            dealing(dealer_hand, card_deck, 1)
            dealer_score = score(dealer_hand)
            
    print "Dealer's hand: ", dealer_hand
    print "Dealer's score: ", dealer_score

    #Determine who won
    if win(player_hand, dealer_hand) == True:
        print "Good work! You win!"
        num_wins += 1
    else:
        print "Sorry! You lose!"
    num_games += 1
    
    print "You have won", num_wins, "out of", num_games, "games."
    keep_playing = raw_input("Enter y to keep playing or n to stop: ")
    print "\n\n\n"
