import random

def player_choise() :
    player_posi = input("Are you BTN or BB")
    return player_posi

def cardDeal():
    BTN_card = random.choice("AQ")
    BB_card = "K"
    return BTN_card, BB_card

def cardOpen(BTN_card, BB_card):
    card_rank = ["Q", "K", "A"]
    BTN_card_rank = card_rank.index(BTN_card)
    BB_card_rank = card_rank.index(BB_card)
    if BTN_card_rank > BB_card_rank:
        winner = "BTN"
    else:
        winner = "BB"
    return winner
    
def betChip(better):
    if better == "BTN":
        bet_history = input("BTN check or bet?:")
        return bet_history
    if better == "BB":
        bet_history = input("BB fold or call?:")
        return bet_history

def takeChipWinner(winner, player_posi, bet_history, player_win_money):
    # posi is BB
    if player_posi == "BTN":
        if bet_history == "check":
            if winner == "BTN":
                player_win_money += 1
            else:
                player_win_money -= 1
        elif bet_history == "fold":
            player_win_money += 1
        elif bet_history == "call":
            if winner == "BTN":
                player_win_money += 3
            else:
                player_win_money -= 3

    if player_posi == "BB":
        if bet_history == "check":
            if winner == "BB":
                player_win_money += 1
            else:
                player_win_money -= 1
        elif bet_history == "fold":
            player_win_money += 1
        elif bet_history == "call":
            if winner == "BB":
                player_win_money += 3
            else:
                player_win_money -= 3
    return player_win_money

def main():
    turn = 1
    player_win_money = 0
    player_posi = player_choise()
    #oponent_money = 10
    while(turn < 10):
        print('turn :', turn)
        # deal cards
        BTN_card, BB_card = cardDeal()
        print("BTN card is " + BTN_card + "| BB card is " + BB_card)

        # BTN bets chip
        better = "BTN"
        bet_history = betChip(better)
        # BB bets chip
        if bet_history == "bet":
            better = "BB"
            bet_history = betChip(better)

        # decide a winner
        winner = cardOpen(BTN_card, BB_card)

        # winner take chips
        player_win_money = takeChipWinner(winner,player_posi, bet_history, player_win_money)

        # turn end
        turn += 1
        print("player_win_money is " + str(player_win_money))
        input('go to next')
    print('thank you')

if __name__ == '__main__':
    main()
