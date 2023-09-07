# Slot machine functionality
import random

STARTING_BALANCE = 0
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

J = 0.5
Q = 1
K = 3
A = 10
TWO_JQ_WIN = 0.1
TWO_K_WIN = 0.3
TWO_A_WON = 1


# Slot machine symbols.
# Getting 3 in a row will win you some $
# 3 'J's will win 50% of amount bet
# 3 'Q's will win 100% of bet amount
# 3 'K's will win 300% of bet amount
# 3 'A' will win 1000% of bet amount


class SlotMachine:
    """
    Slot Machine Class
    Methods:
        check_win - check if the player won
        get_bet - get the bet
        slot_machine_spin - spin the slot machine
        deposit - deposit
        update_balance - update balance
        cash_out - cash out
    """

    def __init__(self):
        with open('data.txt', 'r') as d:  # read the data file that may contain the balance
            self.balance = int(d.read())  # set as initial balance
        if self.balance < 0:
            self.balance = 0
        self.symbols = ["J", "J", "J", "J", "Q", "Q", "Q", "K", "K", "A"]
        random.shuffle(self.symbols)

    def number_of_lines(self) -> int:
        """
        This function will only accept an integer from the user, otherwise,
        it will keep prompting for an input until an integer is provided.
        Prompts the user for the number of lines they want to bet on (1-3).
        :return: int: The number of lines to bet on.
        """
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

    def get_bet(self) -> int:
        """
        This function will only accept an integer from the user, otherwise,
        it will keep prompting for an input until an integer is provided.
        Prompts the user for the amount they want to bet per line.
        :return: int: The amount to bet.
        """
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

    def slot_machine_spin(self) -> list:
        """
        This function generates a payline of symbols to display to the player.
        It does so by using the random module to randomly select 3 items from a pre-defined list of symbols.
        :return: list: The payline of symbols
        """
        spin = []
        for _ in range(3):
            symbol = random.choice(self.symbols)
            spin.append(symbol)
        return spin

    def deposit(self) -> int:
        """
        This function takes deposits. The amount entered must be an integer.
        :return: int: The amount deposited.
        """
        while True:
            player_deposit = input("Enter an amount to deposit:\n $")
            if player_deposit.isdigit():
                player_deposit = int(player_deposit)
                break
            else:
                print("Please enter a valid $ amount.")
        return player_deposit

    def update_balance(self, total_bet: int) -> int:
        """
        Updates the balance. It updated the data.txt file with the new balance
        :param total_bet: int
        :return: int: The updated balance
        """
        with open("data.txt", 'r') as d:
            self.balance = int(d.read()) - total_bet
        with open("data.txt", 'w') as d:
            d.write(str(self.balance))
        return self.balance

    def cash_out(self) -> None:
        """
        After typing 'cash out' in the game prompt, the program will immediately end.
        All variables will be reset to their initial values.
        Balance will be reset to 0
        :return:
        """
        print(f"You have cashed out ${self.balance}, your play balance is $0.")
        with open("data.txt", 'w') as d:
            d.write(str(0))

    def check_win(self, spin: list, total_bet: int):
        """
        Checks if a winning payline has been generated.
        :param spin: list: The payline of symbols
        :param total_bet: int: The amount bet
        :return: None
        """
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
