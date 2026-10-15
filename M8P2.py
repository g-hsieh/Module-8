print("Begin displaying the first 20 numbers by using the Fibonacci sequence.")
print()

firstNumber = 1
secondNumber = 2

for count in range(20):
    print(firstNumber)

    nextNumber = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = nextNumber