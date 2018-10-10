play1 = 0
play2 = 0
numgames = 0
p1score = 0
p2score = 0
#sets all scores and counters as 0, so that it can += 1 later on. 

while play1 != "rock" and play1 != "paper" and play1 != "scissors" and play1 != "stop": 
    play1 = raw_input("Player 1, please input either rock, paper, or scissors. Type stop if you want to stop playing: ")
    if play1 == "stop":
        print "Player 1 has stopped the game without playing any games." 
#this forces the first player to input rock, paper, scissors, or stop so that there are no errors in their input, and keeps them in the while loop until they input a good value.

#if the first player simply inputs stop, then it will end the game without any scores displayed.
if play1 != "stop":
    for i in range(1,25):
        print "\n"
#if the first player inputs rock, paper, or scissors, then it will skip spaces so that the second player cannot see the first player's inputs.
    
    while play2 != "rock" and play2 != "paper" and play2 != "scissors" and play2 != "stop":     
        play2 = raw_input("Player 2, please input either rock, paper, or scissors. Type stop if you want to stop playing: ")
        if play2 == "stop":
            print "Player 2 has stopped the game without playing any games."
#this forces the second player to do the same as the first player.

#again, if the first player simply inputs stop, then it will end the game without keeping any scores.
    if play2 != "stop":
        while play1 == "rock" or play1 == "paper" or play1 == "scissors":
            if play1 == "rock":
                if play2 == "paper":
                    print "Player 1 played rock. Player 2 played paper."
                    print "Player 2 wins!"
                    p2score += 1
                    numgames += 1
#if the second player does not input stop, and the first player inputs rock, paper, or scissors, then it will display the specific outcome of this match.

#after the match, the second player wins, and one more game is played, adding += 1 to the score and game counter.
                elif play2 == "scissors":
                    print "Player 1 played rock. Player 2 played paper."
                    print "Player 1 wins!"
                    p1score += 1
                    numgames += 1
#if the second player inputs scissors, then it will display the specific outcome of the match.

#after the match, the first player wins, and one more game is played, adding += 1 to the score and game counter.
                elif play2 == "rock":
                    print "Player 1 played rock. Player 2 also played rock."
                    print "It's a tie!"
                    numgames += 1
#if the second player inputs rock, then it will display the specific outcome of the match.

#after the match, both players win, so there will be no score increase, but there will still be a game count increase.
            if play1 == "paper":
                if play2 == "rock":
                    print "Player 1 played paper. Player 2 played rock."
                    print "Player 1 wins!"
                    p1score += 1
                    numgames += 1
#if the first player inputs paper, and the second player inputs rock, then it will display the specific outcome of the match.

#after the match, the first player wins, and one more game is played, adding += 1 to the score and game counter.
                elif play2 == "scissors":
                    print "Player 1 played paper. Player 2 played scissors."
                    print "Player 2 wins!"
                    p2score += 1
                    numgames += 1
#if the second player inputs scissors, it displays the specific outcome of the match.

#after the match, the second player wins, and one more game is player, adding += to the score and game counter.
                elif play2 == "paper":
                    print "Player 1 played paper. Player 2 also played paper."
                    print "It's a tie!"
                    numgames += 1
            if play1 == "scissors":
                if play2 == "rock":
                    print "Player 1 played scissors. Player 2 played rock."
                    print "Player 2 wins!"
                    p2score += 1
                    numgames += 1
                elif play2 == "paper":
                    print "Player 1 played scissors. Player 2 played paper."
                    print "Player 1 wins!"
                    p1score += 1
                    numgames += 1
                elif play2 == "scissors":
                    print "Player 1 played scissors. Player 2 also played scissors."
                    print "It's a tie!"
                    numgames +=1
#the same as above applies to this if statement, too.
          
          play1 = play2 = 0
            while play1 != "rock" and play1 != "paper" and play1 != "scissors" and play1 != "stop": 
                play1 = raw_input("Player 1, please input either rock, paper, or scissors again. Type stop if you want to stop playing: ")
            if play1 == "stop":
                print "Player 1 has stopped the game. Player 1 won %s game(s), and Player 2 won %s game(s). %s game(s) total were played." %(p1score, p2score, numgames)
#this outcome occurs after a match. The first player has the option to continue playing, or stop and see the conclusion of the game.       
            if play1 != "stop":
                
                for i in range(1,25):
                        print "\n"
#if they first player inputs rock, paper, or scissors, then it will skip spaces so that the second player cannot see the first player's inputs.
            
            if play1 != "stop":
                while play2 != "rock" and play2 != "paper" and play2 != "scissors" and play2 != "stop": 
                    play2 = raw_input("Player 2, please input either rock, paper, or scissors again. Type stop if you want to stop playing: ")
            if play2 == "stop":
                    print "Player 2 has stopped the game. Player 1 won %s game(s), and Player 2 won %s game(s). %s game(s) total were played." %(p1score, p2score, numgames)
#this outcome occurs after a match, and after the first player has inputted rock, paper, or scissors. The second player has the option to respond to the first player's choice, or stop and see the conclusion of the game. 
