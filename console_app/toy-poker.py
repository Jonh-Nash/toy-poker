import random

def bot_actions(bot_posi, BTN_card, BB_card):
    if bot_posi == "BTN":
        if BTN_card == "A":
            action = "bet"
        if BTN_card == "Q":
            action = random.choice(["check", "bet"])
    if bot_posi == "BB":
        action = random.choice(["call", "fold"])

    return action

def player_choise() :
    player_posi = input("Are you BTN or BB")
    return player_posi

def cardDeal(AQlist):
    #BTN_card = random.choice(AQlist)
    BTN_card = AQlist.pop()
    BB_card = "K"
    return BTN_card, BB_card, AQlist

def cardOpen(BTN_card, BB_card):
    card_rank = ["Q", "K", "A"]
    BTN_card_rank = card_rank.index(BTN_card)
    BB_card_rank = card_rank.index(BB_card)
    if BTN_card_rank > BB_card_rank:
        winner = "BTN"
    else:
        winner = "BB"
    return winner
    
def betChip(better, player_posi, bot_action):
    if better == "BTN":
        if player_posi == "BTN":
            bet_history = input("BTN check or bet?:")
            return bet_history
        else:
            bet_history = bot_action
            return bet_history
    if better == "BB":
        if player_posi == "BB":
            bet_history = input("BB call or fold?:")
            return bet_history
        else:
            bet_history = bot_action
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
            player_win_money -= 1
        elif bet_history == "call":
            if winner == "BB":
                player_win_money += 3
            else:
                player_win_money -= 3
    return player_win_money

def main():
    turn = 1
    player_win_money = 0
    # decide position
    player_posi = "BB"
    bot_posi = "BTN"
    # make card box
    AQlist = ["A"] * 25 + ["Q"] * 25
    random.shuffle(AQlist)
    #oponent_money = 10
    while(turn < 10):
        turn_flag = False
        print('turn :', turn)
        # deal cards
        BTN_card, BB_card, AQlist = cardDeal(AQlist)
        print("BTN card is " + BTN_card + "| BB card is " + BB_card)

        # decide bot action
        bot_action = bot_actions(bot_posi, BTN_card, BB_card)

        # BTN bets chip
        better = "BTN"
        bet_history = betChip(better, player_posi, bot_action)
        print("BTN " + bet_history)
        # BB bets chip
        if bet_history == "bet":
            better = "BB"
            bet_history = betChip(better, player_posi, bot_action)
            print("BB " + bet_history)
        

        # decide a winner
        winner = cardOpen(BTN_card, BB_card)

        # winner take chips
        player_win_money = takeChipWinner(winner,player_posi, bet_history, player_win_money)

        # turn end
        turn += 1
        print("player_win_money is " + str(player_win_money))
        turn_flag = True
        input('go to next')
    print('thank you')

if __name__ == '__main__':
    main()
