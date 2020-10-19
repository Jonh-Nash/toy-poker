import random

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

def takeChipWinner(winner, bet_history):
    if bet_history == "check":
        print(winner + " takes 1bb with ")
    if bet_history == "fold":
        print("BTN" + " takes 1bb with")
    if bet_history == "call":
        print(winner + " takes 3bb with")

def main():
    turn = 1
    player_money = 10
    oponent_money = 10
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
        takeChipWinner(winner, bet_history)

        # turn end
        turn += 1
        input('go to next')
    print('thank you')

if __name__ == '__main__':
    main()
