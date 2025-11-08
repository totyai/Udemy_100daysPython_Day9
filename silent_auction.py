"""
Build a blind auction
- print ASCI art
- Welcome
- Ask name
- What is the bid?
- Is ther other bidder? -should add name and bid
- Until asking if there is other bid
- print out the the hieghts

Clear terminal with 100 new lines between bids
"""

gavel = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
bids = {}
more_bids = True
welcome = "Welcome to the silent auchion, where each contendents needs to give a bid, and the highest bid will win."
highest_bidder = ""

print(f"{gavel} \n {welcome}")
while more_bids:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    bids[name] = bid

    more_bidder = input("Are there any other bidders? Type 'yes' or 'no'")
    if more_bids.lower() == "yes":
        more_bids = True
    elif more_bids.lower() == "no":
        more_bids = False
    else:
        print("Incorrect, the program exits.")
        break

# TODO - capture highest bidder, run through dict
for name in bids:
    pass