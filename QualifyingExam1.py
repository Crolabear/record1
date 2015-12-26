from __future__ import division
import random

# I want to make it like a c program.
# so this will mean i will define class and main??

class Problem1(object):
    def __init__(self):
        self.ans = 99
        
        
    def sim(self,n, p1,p2):
        # n = number of tosses
        # p = probability of head, to keep it simple,  we will let p1 be the numerator, p2 be the denominator
        # k = number of iterations.
        r=[]
        for item in range(n):
            tem=random.randint(0,p2-1)
            if tem < p1:
                r.append(1)
            else:
                r.append(0)
        # so now i generated a list of head and tails.
        # then I need to count the number of times it changes from head to tail.
        count = 0
        currentStat = 99
        for item in r:
            if item != currentStat:
                count = count + 1
                currentStat = item
    #print r
        return count	
#    
#    def estimate(self,n,p1,p2, number_repeat=100):
#        result = []
#        for item in range(number_repeat):
#            k1 = sim(n,p1,p2)
#            print k1
#            result.append(k1)
#        self.ans = sum(result)/number_repeat
#        #print result
#        return self.ans



# use main to run the simulation

# too slow tho. how do i speed it up
def main():
    prob1 = Problem1()
    prob1.__init__()
    n = 100000
    number_toss=8
    p1 = 1
    p2 = 4
    result = []
    for item in range(n):
        result.append(prob1.sim(number_toss,p1,p2))

    print sum(result)/n


if __name__ == "__main__":
    main()





