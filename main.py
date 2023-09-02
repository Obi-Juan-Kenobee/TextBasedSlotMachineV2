# Text based slot-machine Version 1.0.0
# Slot machine only displays one line of symbols in its current version.
# Future versions will add more functionality.
# Written using procedural programming with Python version 3.11

import random

# Global variables for bets, lines and symbol chart for winnings
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
symbols = ["J", "J", "J", "J", "Q", "Q", "Q", "K", "K", "A"]

TWO_JQ_WIN = 0.1
TWO_K_WIN = 0.3
TWO_A_WIN = 1

# Slot machine symbols.
# Getting 3 in a row will win you some $
# 3 'J's will win 50% of amount bet
J = 1.5
# 3 'Q's will win 100% of bet amount
Q = 2
# 3 'K's will win 300% of bet amount
K = 3
# 3 'A' will win 1000% of bet amount
A = 10


def number_of_lines():  # This function will only accept an integer from the user, otherwise,
    # it will keep prompting for an input until an integer is provided.
    while True:
        lines_to_bet_on = input("How many lines do you want to bet on (1-3)?\n")
        if lines_to_bet_on.isdigit():
            lines_to_bet_on = int(lines_to_bet_on)
            if 1 <= lines_to_bet_on <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines_to_bet_on


def get_bet():  # This function will only accept an integer from the user, otherwise,
    # it will keep prompting for an input until an integer is provided.
    while True:
        bet = input("How much would you like to bet per line?\n $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a valid $ amount between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a valid $ amount.")
    return bet


def slot_machine_spin():  # This function generates a payline of symbols to display to the player.
    # It does so by using the random module to randomly select 3 items from a pre-defined list of symbols.
    # In this game version, it only allows for one payline to be generated.
    spin = []
    for _ in range(3):
        symbol = random.choice(symbols)
        spin.append(symbol)
    return spin


def deposit():  # This function takes deposits. The amount entered must be an integer.
    # Floating point numbers can be typed in as well, however, in its current version,
    # the slot machine does not perform any operations where floats are necessary.
    while True:
        player_deposit = input("Enter an amount to deposit:\n $")
        if player_deposit.isdigit():
            player_deposit = int(player_deposit)
            break
        else:
            print("Please enter a valid $ amount.")
    return player_deposit


def cash_out(balance):  # After typing 'cash out' in the game prompt, the program will immediately end.
    # All variables will be reset to their initial values.
    # It needs the balance to be passed as an argument.
    print(f"You have cashed out ${balance}, your play balance is now $0.")


def check_win(spin, total_bet):  # Checks if a winning payline has been generated.
    # Please refer to the symbol chart above for values of each potential win.
    # The payline 'spin' and the total bet are required in this function.
    if spin[0] == "Q" and spin[1] == "Q" and spin[2] == "Q":
        print(f"You have won ${total_bet * Q}")
        winnings = total_bet * Q
        return winnings

    elif spin[0] == "J" and spin[1] == "J" and spin[2] == "J":
        print(f"You have won ${total_bet * J}")
        winnings = total_bet * J
        return winnings

    elif spin[0] == "K" and spin[1] == "K" and spin[2] == "K":
        print(f"You have won ${total_bet * K}")
        winnings = total_bet * K
        return winnings
    elif spin[0] == "A" and spin[1] == "A" and spin[2] == "A":
        print(f"You have won ${total_bet * A}")
        winnings = total_bet * A
        return winnings
    else:
        if spin.count('J') == 2 or spin.count('Q') == 2:
            print(f"You win ${total_bet * TWO_JQ_WIN}")
            winnings = total_bet * TWO_JQ_WIN
            return winnings
        elif spin.count('K') == 2:
            print(f"You win ${total_bet * TWO_K_WIN}")
            winnings = total_bet * TWO_K_WIN
            return winnings
        elif spin.count("A") == 2:
            print(f"You win ${total_bet * TWO_A_WIN}")
            winnings = total_bet * TWO_A_WIN
            return winnings
        else:
            print("No win.")
            return None


# Welcome messages and prompts for the players
print('Welcome to Vegas Slots!')
print("At any time type 'balance' to see your play balance.")
print("Type 'cash out' to cash out your winnings.")


def main():  # Runs the whole game logic.
    balance = 0  # Only needed for the print statement below.
    print(f"Your initial balance is {balance}")
    balance = deposit()
    print(f"Your balance is now ${balance}")
    while True:  # This while loop will keep the game going as long as the player does not 'cash out'.
        # "Play" will run the slot machine, "Balance" will display current balance,
        # "Deposit" will call the deposit function defined above, and "Cash Out" will exit the game.
        player = input("What do you want to do?\n [Play] [Cash Out] [Balance] [Deposit]\n ").lower()
        if player == "play":
            lines = number_of_lines()
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(
                    f"Your balance is too low to make that bet. Your current balance is ${balance}.\nAnd your current "
                    f"bet is ${total_bet}")
            else:
                print(f"You are betting ${bet} on {lines} lines. \nYour total bet is ${total_bet}")
                spin = slot_machine_spin()
                balance -= total_bet
                winnings = check_win(spin, total_bet)
                if winnings is None:
                    balance -= total_bet
                else:
                    balance += winnings
                print(spin)

        elif player == "cash out":
            print(f"You have cashed out your balance of ${balance}, your play balance is now $0.")
            print("Thank you for playing Vegas Slots.")
            break

        elif player == "balance":
            print(f"Your current play balance is ${balance}")

        elif player == "deposit":
            new_deposit = deposit()
            balance += new_deposit
            print(f"Deposit accepted \nYour new play balance is now {balance}")

        else:
            print("Sorry, that is not a recognized command. Please choose a command from available options.")


main()