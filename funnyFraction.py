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

    return (count,newT1,newT2)  # only returns the unique elements


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



def combineTopBot(topTuple,botTuple):
    topList = map(tuple,itertools.permutations(topTuple))
    botList = map(tuple,itertools.permutations(botTuple))
    g = [(x, y) for x in topList for y in botList]   # this produce the cross product of the two lists.
    #g = ((x, y) for x in topList for y in botList)   
    return g
	# this produce the cross product of the two lists, but as a generator
	

# the problem is i dont know how to access the elements.


def checkDigitInNumber(digitList,NumberStr):
	count = 0
	for item in digitList:
		if str(item) in str(NumberStr):
			count = count + 1
	result = 0
	if count == len(digitList):
		result = 1
	return result



def checkFraction(topTuple,botTuple):
    checkCommonTop = removeDup(topTuple,botTuple) # make sure topTUple is the same length as the bot tuple
    result = []
    if checkCommonTop[0] == len(topTuple):  # that means no common digits
        return (0,0) # this means we dont have any cancellation we can use. not the fraction we are looking for.
    else:  # if we do have some common digits, we can proceed.
        crossProduct1 = combineTopBot(topTuple,botTuple)
        #print crossProduct1    
        r1 = map(lambda x:simplifyFraction(x[0],x[1]),crossProduct1)
        
        # create a dictionary that connects the simplified fraction and the tuple:
        dict1 = {}
        for i in range(len(r1)):
        	dict1[r1[i]] = crossProduct1[i]
        	
        for item2 in r1:
    		t1 = checkDigitInNumber(checkCommonTop[1],item2[0])
    		#print t1
    		b1 = checkDigitInNumber(checkCommonTop[2],item2[1])
#     		print b1*t1
    		if (t1*b1) == 1:
    			result.append(dict1[item2])
    return result
    			



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



