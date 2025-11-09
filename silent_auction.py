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

def main():
    global bids, more_bids, welcome, highest_bidder
    print(f"{gavel} \n {welcome}")
    while more_bids:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        bids[name] = bid

        more_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        if more_bidder.lower() == "yes":
            more_bidder = True
            for i in range(100):
                print("\n")
        elif more_bidder.lower() == "no":
            more_bids = False
        else:
            print("Incorrect, the program exits.")
            return

    # TODO - capture highest bidder, run through dict
    for name in bids:
        try:
            if bids[name] > bids[highest_bidder]:
                highest_bidder = name
        except:
            highest_bidder = name
    print(f"The winner is {highest_bidder} with bid of ${bids[highest_bidder]}.")

if __name__ == "__main__":
    main()