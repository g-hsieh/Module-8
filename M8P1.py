print ("This program will help you display your interest earnings in five years after you enter the inital principal and the annual interest rate.")
print()

runProgram = input("Would you like to know your earnings after 5 years? (Yes/No): ")

while runProgram.lower() in ("yes", "y"):

    Principle = float(input("What's the principal amount? "))
    InterestRate = float(input("What's the interest rate (as a percentage)? "))

    BeginningBalance = Principle
    AccumulatedInterest = 0

    print()
    print(f"{'Year':<6}{'Beginning':>16}{'Ending':>16}")
    print(f"{'':<6}{'Balance':>16}{'Balance':>16}")
    print("-" * 39)

    for YearCount in range(1, 6):

        AnnualInterest = BeginningBalance * (InterestRate / 100)
        EndingBalance = BeginningBalance + AnnualInterest

        AccumulatedInterest += AnnualInterest

        
        print(f"{YearCount:>6}{('$' + format(BeginningBalance, ',.2f')):>16}{('$' + format(EndingBalance, ',.2f')):>17}")

        BeginningBalance = EndingBalance

    print()
    print(f"Total interest earned: ${AccumulatedInterest:,.2f}")

    print()
    runProgram = input("Would you like to enter a different principal? (Yes/No): ")

print("Program ended. Thank you for stopping by.")