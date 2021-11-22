from replit import clear

LOGO = """

"""

bids = {}
bidding_finished = False


def find_highest_amount(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, won with ${highest_bid}")


while not bidding_finished:
    name = input("What's your name?: ").title()
    user_bid = int(input("What's your bid? $ "))
    bids[name] = user_bid
    res = input("Are there any other bidders? ").lower()
    if res == "no":
        bidding_finished = True
        find_highest_amount(bids)
    elif res == "yes":
        clear()

