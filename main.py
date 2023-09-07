# Text based slot-machine Version 2.0.0
# Slot machine only displays one line of symbols in its current version.
# Written using Python version 3.11

from slot_machine import *

slot_machine = SlotMachine()

# Welcome messages and prompts for the players
print('Welcome to Vegas Slots!')
print("At any time type 'balance' to see your play balance.")
print("Type 'cash out' to cash out your winnings.")


def main():  # Runs the whole game logic.
    balance = 0  # Only needed for the print statement below.
    print(f"Your initial balance is {balance}")
    balance = slot_machine.deposit()
    print(f"Your balance is now ${balance}")
    while True:  # Main game loop
        player = input("What do you want to do?\n [Play] [Cash Out] [Balance] [Deposit]\n ").lower()
        if player == "play":
            lines = slot_machine.number_of_lines()
            bet = slot_machine.get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(
                    f"Your balance is too low to make that bet. Your current balance is ${balance}.\nAnd your current "
                    f"bet is ${total_bet}")
            else:
                print(f"You are betting ${bet} on {lines} lines. \nYour total bet is ${total_bet}")
                spin = slot_machine.slot_machine_spin()
                balance -= total_bet
                winnings = slot_machine.check_win(spin, total_bet)
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
            new_deposit = slot_machine.deposit()
            balance += new_deposit
            print(f"Deposit accepted \nYour new play balance is now {balance}")

        else:
            print("Sorry, that is not a recognized command. Please choose a command from available options.")


main()
