import random


class color:
    BOLD = "\033[1m"
    END = "\033[0m"


def check(Number, Scale):
    Scale = int(Scale)
    if Number > Scale:
        Scale = str(Scale)
        print(
            color.BOLD
            + "You entered a number higher than the range you choose"
            + color.END
            + " , try to enter a number equal to or below "
            + Scale
        )
        print(guess(Scale, Number))
    if Number < 0:
        print(
            color.BOLD
            + "You entered a number lower than Zero,try to enter a number higher than Zero"
            + color.END
        )
        print(guess(Scale, Number))
    else:
        print(guess(Scale, Number))


def guessA(b, Number2):
    b = int(b)
    if b < Number2:
        try:
            Number2 = int(input("High, Guess again:"))
            return guessA(b, Number2)
        except ValueError:
            print("Sorry, I didn't understand that.")
    if b > Number2:
        try:
            Number2 = int(input("Low, Guess again:"))
            return guessA(b, Number2)
        except ValueError:
            print("Sorry, I didn't understand that.")
    if b == Number2:
        return "You guessed correctly."


def guess(Scale, Number):
    Scale = int(Scale)
    a = random.randint(0, Scale)
    a = int(a)
    if a < Number:
        b = a
        try:
            Number2 = int(input("High, Guess again:"))
            return guessA(b, Number2)
        except ValueError:
            print("Sorry, I didn't understand that.")
    if a > Number:
        b = a
        try:
            Number2 = int(input("Low, Guess again:"))
            return guessA(b, Number2)
        except ValueError:
            print("Sorry, I didn't understand that.")
    if a == Number:
        return "You guessed correctly."


try:
    Scale = int(input("A random number will be generated between zero and: "))
    Scale = str(Scale)
    if Scale[0] == "-":
        print(
            color.BOLD
            + "You must enter a positive number for your previous selection, if you continue there will be an error"
            + color.END
        )
except ValueError:
    print("Sorry, I didn't understand that.")
except NameError:
    print("You have not entered a number.")
try:
    Number = int(
        input(
            "A random number has been generated between 0 and "
            + Scale
            + ",guess what the number is:"
        )
    )
    check(Number, Scale)
except NameError:
    print("You have not entered a number.")
except ValueError:
    print("Sorry, I didn't understand that.")
