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
    			



def restorDigit2Number(tuple1):
	a=0
	n = len(tuple1)
	for i in range(n):
		a=a+(10**i)*tuple1[i]
	return a


def isSubset(bigNum,shortNum):
	a = str(bigNum)
	count = 0
	for item in str(shortNum):
		if item in a:
			count = count + 1
	if count == len(str(shortNum)):
		return 1
	else:
		return 0
		
def isExactMatch(bigNum,shortNum):
	a = []
	b=[]
	for item in str(bigNum):
		a.append(item)
	for item2 in str(shortNum):
		b.append(item2)
	a.sort()
	b.sort()
	if a == b:
		return 1
	else:
		return 0		

def findSharedDigits(num1,num2):
	count =0
	for item in str(num1):
		if item in str(num2):
			count = count + 1
	if count > 0:
		return 1
	else:
		return 0


def removeSharedDigits(num1,num2):
	shared = []
	a = str(num1)
	b = str(num2)
	for item in a:
		if item in b:
			shared.append(item)
	for item1 in b:
		if item1 in a:
			shared.append(item1)
	shared1 = list(set(shared))
	a1 = a
	b1 = b
	for item2 in shared1:
		a1=a1.replace(item2,'')
		b1=b1.replace(item2,'')
	if a1 == '' or b1 =='':
		a1 = 0
		b1 = 0
	
	return (int(a1),int(b1))

# it looks like checking digit doesn't work.
# let's do brute force it


def bruteForce(sizeFraction):
	begin = 10**(sizeFraction - 1)
	end = 10 ** (sizeFraction)
	list1 = range(begin, end)
	# maybe we want to edit this to remove numbers containing 0?
	
	xproduct1 = []
	xproduct = list(itertools.product(list1,list1))
	for item in xproduct:
		if (item[0] < item[1]) and (item[1]%10 >0):
			test = findSharedDigits(item[0],item[1])
			if test == 1:
				xproduct1.append(item)
	# only consider numbers with shared digit
	
	# then I want to divide and find the 
	GCF=map(lambda x:EulerAlgo(x[0],x[1]),xproduct1)
	
	result = []
	for i in range(len(GCF)):
		if GCF[i] != 1:
			t1 = xproduct1[i][0]/GCF[i]
			b1 = xproduct1[i][1]/GCF[i]
			
			simtop,simbot = removeSharedDigits(xproduct1[i][0],xproduct1[i][1])
			a1 = isExactMatch(simtop,t1)
			a2 = isExactMatch(simbot,b1)
			#a1=isSubset(simtop,t1) 
			#a2=isSubset(simbot,b1)
			#a1=isSubset(xproduct1[i][0],t1)
			#a2=isSubset(xproduct1[i][1],b1)
			if a1*a2 == 1:
				result.append(xproduct1[i])
				print xproduct1[i]
	return result
	
	

	
	
	
	
	
	