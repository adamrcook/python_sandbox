# change.py
#   A program to calculate the value of some change in dollars


def main():
    print "Change Counter"
    print
    print "Please enter the count of each coin type." 
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickles = input("Nickles: ")
    pennies = input("Pennies: ")
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    print
    print "The total value of your change is", total

main()


