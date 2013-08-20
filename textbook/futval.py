# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future


def main():
    print "This program calculates the future value of a 10-year investment."
    
    years = input("Enter the term, in years: ")
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualzied interest rate: ")
    inflation = input("Enter an assumption for the inflation rate: ")
        
    for i in range(years):
        principal = (principal * (1 + apr))/(1 + inflation)
#        principal = principal * (1 + apr)
    print "The amount in", years, "years is:", principal

main()