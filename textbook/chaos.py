def main():
    print "this program illustrates a chaotic function "
    x = input("Enter a number between 0 and 1: ")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print x
        
main()