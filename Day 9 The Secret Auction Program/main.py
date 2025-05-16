bidding = False
bid = {}
while not bidding:
    name = input("Enter bidding name: ")
    price = input("Enter bidding price: ")
    bid[name] = price
    bidding = input("Do you want to bid? yes or no: ")
    if bidding == "yes":
        bidding = True
    else:
        bidding = False

print(bid)








# from art import logo
# print(logo)
#
# bidding_finished = False
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
# bids = {}
# while not bidding_finished:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)