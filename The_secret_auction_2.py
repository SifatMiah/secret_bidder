from art import art_a

print(art_a)

bid = {}

def find_highest_bidder(bid_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bidding amount is ${highest_bid}")


continue_game = True
while continue_game:
    name = input("What is the name of the bidder? ")
    price = float(input("What is the bid amount? $"))
    bid[name] = price
    should_continue = input("Type 'yes' if you have more bidder or type 'no' if you don't have  ").lower()
    if should_continue == "no":
        continue_game = False
        find_highest_bidder(bid)


    if should_continue == "yes":
        print("\n" * 100)
