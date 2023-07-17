import random

piece={"Mona Lisa":1500,"Starry Night":1000,"Venus de Milo":15_000,"Tomb of Alexander":50_000,"Holy Family":2000}

piece_list=[]
for z in piece.items():
    piece_list.append(z)
one_piece=random.choice(piece_list)

piece_name=[]
piece_price=[]
piece_name.append(one_piece[0])
piece_price.append(one_piece[1])
print("This piece is",*piece_name,"and it's price",*piece_price)

def auction_list(name_x,bid_x):
    dict={}
    dict["name"]=name_x
    dict["bid"]=bid_x
    return dict

bidders=[]
auction=True
while auction:
    name=input("What is your name?: ")
    auction2=True
    while auction2:
        bid=int(input("What is your bid: $"))
        if bid<piece_price[0]:
            print("Please enter a balance above the lower limit.")
        if bid>=piece_price[0]:
            auction2=False
            bidder_exists = False
            for bidder in bidders:
                if bidder["name"] == name:
                    bidder["bid"] = bid
                    bidder_exists = True
                    break
            if not bidder_exists:
                bidders.append(auction_list(name, bid))
            yes_no=input("Are there any other bidders? Type 'yes' or 'no'.\n")
            if yes_no=="no":
                auction=False

high_bid=0
for bidder in bidders:
    if bidder["bid"]>high_bid:
        high_bid = bidder["bid"]
        winner_bid=bidder["name"]
print("Here are the bidders:")
for bidder in bidders:
    print(f"Name: {bidder['name']}, Bid: ${bidder['bid']}")
print(f"The winner is {winner_bid} with a bid of ${high_bid}")



