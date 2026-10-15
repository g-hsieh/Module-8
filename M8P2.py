print("Begin displaying the first 20 numbers by using the Fibonacci sequence.")
print()

firstNumber = 0
secondNumber = 1

for count in range(20):
    print(firstNumber)

    nextNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = nextNumber