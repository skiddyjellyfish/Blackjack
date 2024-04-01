def Blackjack():
    from random import shuffle
    
    from time import sleep

    #All cards are at face value, except for the King, Queen and Jack which count as 10. An Ace will have a value of 11 unless that would give a player or the dealer a score in excess of 21; in which case, it has a value of 1. The dealer starts the game. Every player gets 2 cards, face up.
    Suits = ["\u2663", "\u2665", 
         "\u2666", "\u2660"] 
    
    Ranks = ['A', '2', '3', '4', '5', 
         '6', '7', '8', '9', '10', 
         'J', 'Q', 'K'] 
    deck = []
    player_hand = []
    dealer_hand = []
    chip_total = 1000
    bet = 1
    pot = 0
    def stand(d_hand, current_score):
        dealer_score = sum_hand(dealer_hand, 0)
        while dealer_score < 17:
            dealer_hand.append(deck.pop())
            dealer_score = sum_hand(dealer_hand, 0)
            if dealer_score == 21:
                print(f"Dealer has {dealer_hand}, for a score of {dealer_score}")
                print("Dealer wins!")
                input("press enter to return.")
                return

        if player_score >= dealer_score:
            print(f"Dealer has {dealer_hand}, for a score of {dealer_score}")
            print("You win!")
            input("press enter to return.")
            return
        elif player_score < dealer_score:
            print(f"Dealer has {dealer_hand}, for a score of {dealer_score}.")
            print("Dealer wins!")
            input("press enter to return.")
            return

    def sum_hand(hand, current_score):
        card_pnt = 0
        point_total = 0
        for card in hand:
            rank = card[:-1]
            if rank in "KQJ":
                card_pnt = 11
            elif rank == "A":
                if current_score >= 11:
                    card_pnt = 1
                else:
                    card_pnt = 11
            else:
                card_pnt = int(rank)
            point_total += card_pnt
        return point_total
    
    for rank in Ranks: 
  
        for suit in Suits: 
            deck.append(rank + suit)
    
    #print(deck)
    shuffle(deck)
    #print(deck)
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    bet = input("What is your bet? ")
    chip_total -= int(bet)
    pot = bet
    player_score = sum_hand(player_hand,0)
    if player_score > 21:
        print("Natural bust! Start again.")
        input("press enter to return.")
        return
    elif player_score == 21:
        print("Natural blackjack!")
        input("press enter to return.")
        return
    
    dealer_score = sum_hand(dealer_hand,0)
    if dealer_score > 21:
        print("Natural dealer bust! Start again.")
        input("press enter to return.")
        return
    elif player_score == 21:
        print("Natural dealer blackjack!")
        input("press enter to return.")
        return
    #sum_hand(['6♥', 'Q♥'], 2)


        

    while player_score < 21:    
        print(f"Player has score of {player_score}, with a {player_hand}")
        print(f"Dealer currently has a {dealer_hand[-1]} and one card hidden.")
        choice = input("Would you like to HIT, STAND, or DOUBLE? ").lower()
        
        if choice == 'hit':
            player_hand.append(deck.pop())
            player_score = sum_hand(player_hand,player_score)
            if player_score == 21:
                print(f"Player has score of {player_score}, with a {player_hand}")
                print("Blackjack!")
                input("press enter to return.")
                return
            elif player_score> 21:
                print(f"Player has score of {player_score}, with a {player_hand}")
                print("Bust!")
                input("press enter to return.")
                return
            
        elif choice == 'stand':
            stand(dealer_hand,player_score)
            return

        elif choice == 'double':
            chip_total -= bet
            pot += bet
            player_hand.append(deck.pop())
            print(f"Player has score of {player_score}, with a {player_hand}")
            player_score = sum_hand(player_hand,player_score)
            if player_score == 21:
                print("Blackjack!")
                input("press enter to return.")
                return
            elif player_score> 21:
                print("Bust!")
                input("press enter to return.")
                return
            


Blackjack()







          