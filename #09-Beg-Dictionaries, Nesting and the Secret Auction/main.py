from art import logo


def clear():
    print("\n" * 130)


def user_bid(bids_list_parameter):
    user = input("What's your name: ")
    bid = float(input("What's your bid: $ "))
    bids_list_parameter[user] = bid
    run_again = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if run_again == 'yes':
        clear()
        user_bid(bids_list_parameter)
    else:
        return


def check_winner(bids_list_parameter):
    winner_name = ""
    winner_bid = 0
    for name in bids_list_parameter:
        if bids_list_parameter[name] > winner_bid:
            winner_name = name
            winner_bid = bids_list_parameter[name]
    clear()
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")


def run_blind_auction():
    print(logo)
    print("\n Welcome to the blind auction.")
    bids_list = {}
    user_bid(bids_list)  # receives the user or users name/bid and add to the bids_list
    check_winner(bids_list)  # check te highest bid at bids_list and declare the winner.
    # print(bids_list)


run_blind_auction()
