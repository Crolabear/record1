# goal: write a program that does the following...
# for any number > 1, divide by 2 if even, and x3+1 if odd.
# figure out how many steps for us to get to 1


# first try:
import sys

class SomeError( Exception ): pass

def OneStep(number, count):
    #number = sys.argv[0]
    if type(number) is int:
        if number%2 is 1:
            number=number*3+1
        else:
            number = number/2
    else:
        ex= SomeError( "Input Not Integer" )
        number =0
        count = 0
        raise ex

    return (number,count+1)

def recur(number,count):
    #num = sys.argv[0]
    #num = 5
    #ct = 0
    if number ==1:
        return (number,count)
    else:
        if number%2 ==1:
            print number
            return recur(number*3+1,count+1)
        else:
            print number
            return recur(number/2,count+1)


def main():
    try:
        num = int(sys.argv[1])
        N,count = recur(num,0)
        print "The number of steps is %d" %(count)
    except ValueError:
        print "Not integer"




if __name__ == "__main__":
    main()