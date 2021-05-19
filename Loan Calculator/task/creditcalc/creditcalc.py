from math import ceil, log
import argparse
import sys


class LoanCalculator:
    principal = None
    payment = None
    periods = None
    interest = None
    args = None
    type = None

    @staticmethod
    def calc_payment():
        principal = LoanCalculator.principal
        periods = LoanCalculator.periods
        nominal_interest = LoanCalculator.interest / (12 * 100)
        LoanCalculator.payment = ceil(principal * nominal_interest * (1 + nominal_interest) ** periods / ((1 + nominal_interest) ** periods - 1))
        overpayment = LoanCalculator.payment * periods - principal
        print(f"Your annuity payment = {LoanCalculator.payment}!")
        print(f"Overpayment = {overpayment}")

    @staticmethod
    def calc_diff_payment():
        nominal_interest = LoanCalculator.interest / (12 * 100)
        principal = LoanCalculator.principal
        periods = LoanCalculator.periods
        payments = []
        for m in range(1, LoanCalculator.periods + 1):
            diff_payment = ceil(principal / periods + nominal_interest * (principal - (principal * (m - 1)) / periods))
            payments.append(diff_payment)
            print(f"Month {m}: payment is {diff_payment}")
        print()
        print(f"Overpayment = {sum(payments) - principal}")

    @staticmethod
    def calc_periods():
        principal = LoanCalculator.principal
        payment = LoanCalculator.payment
        nominal_interest = LoanCalculator.interest / (12 * 100)
        LoanCalculator.periods = ceil(log(payment / (payment - nominal_interest * principal), 1 + nominal_interest))
        years = LoanCalculator.periods // 12
        months = LoanCalculator.periods % 12

        print(f"It will take{' ' + str(years) + ' years and'}{' ' + str(months)}"
              f"{' months' if ceil(principal / payment) > 1 else ' month'}"
              f" to repay the loan!")
        print(f"Overpayment = {LoanCalculator.periods * payment - principal}")

    @staticmethod
    def calc_principal():
        payment = LoanCalculator.payment
        periods = LoanCalculator.periods
        nominal_interest = LoanCalculator.interest / (12 * 100)
        LoanCalculator.principal = payment / (nominal_interest * (1 + nominal_interest) ** periods / ((1 + nominal_interest) ** periods - 1))

        print(f"Your loan principal = {LoanCalculator.principal}")

    @staticmethod
    def parse_input():
        parser = argparse.ArgumentParser()
        parser.add_argument("--type", choices=["annuity", "diff"])
        parser.add_argument("--payment")
        parser.add_argument("--principal")
        parser.add_argument("--periods")
        parser.add_argument("--interest")
        LoanCalculator.args = parser.parse_args()

    @staticmethod
    def check_validity():
        args = LoanCalculator.args
        incorrect = False
        if args.type not in ['annuity', 'diff'] or (args.type == "diff" and args.payment is not None):
            incorrect = True

        if len(sys.argv) != 5:
            incorrect = True

        if args.interest is None:
            incorrect = True

        if args.principal is not None and int(args.principal) < 0:
            incorrect = True

        if args.periods is not None and int(args.periods) < 0:
            incorrect = True

        if args.interest is not None and float(args.interest) < 0:
            incorrect = True

        if args.payment is not None and float(args.payment) < 0:
            incorrect = True

        if incorrect:
            print("Incorrect parameters")
            exit()
        else:
            LoanCalculator.principal = int(args.principal) if args.principal is not None else None
            LoanCalculator.periods = int(args.periods) if args.periods is not None else None
            LoanCalculator.payment = int(args.payment) if args.payment is not None else None
            LoanCalculator.interest = float(args.interest) if args.interest is not None else None
            LoanCalculator.type = args.type

    @staticmethod
    def choose_program():
        if LoanCalculator.type == "diff":
            LoanCalculator.calc_diff_payment()
        elif LoanCalculator.type == "annuity":
            if LoanCalculator.periods is None:
                LoanCalculator.calc_periods()
            elif LoanCalculator.payment is None:
                LoanCalculator.calc_payment()
            elif LoanCalculator.principal is None:
                LoanCalculator.calc_principal()


def main():
    LoanCalculator.parse_input()
    LoanCalculator.check_validity()
    LoanCalculator.choose_program()


main()
