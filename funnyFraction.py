import itertools

#def generateNumbers(number_unique):
	

def scrambleNumber(number_unique):
	# require itertool
	number = [1,2,3,4,5,6,7,8,9]
	# this line gives me a list of tuples, each element is a subset of the set number 
	# we fix the size of the subset by parameter number_unique
	combo = map(tuple,itertools.combinations(number,number_unique))
	
	# then let's create another combo
	allOrdering = map(tuple,itertools.permutations(range(number_unique)))
	
	# then I can check for equalities.
	return combo


def EulerAlgo(N1,N2):
    while (N2 != 0):
        t = N2
        N2 = N1%N2
        N1 = t
    return N1


def removeDup(tuple1,tuple2):
    temp = []
    count = 0
    # only 1 way copmarison.
    for item in tuple1:
        if item in tuple2:
            temp.append(item)
        else:
            count = count + 1
    
    newT1 = list(y for y in tuple1 if y not in temp)
    newT2 = list(y for y in tuple2 if y not in temp)

#    for item2 in tuple2:
#        if item2 not in tuple1:
#            temp.append(item2)

    return (count,newT1,newT2)


def simplifyFraction(topT,botT):
    # calls EUlerAlgo function
    tNum = 0
    bNum = 0
    for i in range(len(topT)):
        tNum = tNum + 10**i*topT[i]
    for i in range(len(botT)):
        bNum = bNum + 10**i*botT[i]

    GCF = EulerAlgo(tNum,bNum)
    if GCF == 1:
        return (0,0)
    else:
        return (tNum/GCF,bNum/GCF)





def checkFraction(topTuple,botTuple):
    checkCommon = removeDup(topTuple,botTuple)
    if checkCommon[0] == 0:  # that means no common digits
        return (0,0) # this means we dont have any cancellation we can use. not the fraction we are looking for.
    else:  # if we do have some common digits, we can proceed.
        uniBot = removeDup(botTuple,topTuple) # need to run it again b/c need to obtain the unique on the bottom
        topList = map(tuple,itertools.permutations(topTuple))
        botList = map(tuple,itertools.permutations(botTuple))
        for L1 in topList:
            for L2 in botList:
                temp = simplifyFraction(L1,L2)
                dup = removeDup(L1,L2)
                count4Top = 0
                count4Bot = 0
                for item1 in dup[1]:
                    if str(item1) in str(temp[0]):
                        count4Top = count4Top + 1
                for item2 in dup[2]:
                    if str(item2) in str(temp[1]):
                        count4Bot = count4Bot + 1
                if (count4Bot == len(dup[2]) and count4Top == len(dup[1])):
                    print temp,L1,L2
                    return (temp)
                else:
                    return 'not work'




def main(sizeFraction):
    count =0
    combDigits=scrambleNumber(sizeFraction)
    for item1 in combDigits:
        for item2 in combDigits:
            if item1 != item2:
                a=checkFraction(item1,item2)
#                if a != (0,0):
#                  print a
                count = count + 1
                if count > 10000:
                    break;
    return 0



