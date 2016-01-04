# the goal of this is to find different ways to add some integers to a specified number within a fix number of operation




def checkDuplicateElements(list1):
    l2 = []
    a=len(list1)
    for k in range(a):
        for item in list1:
            if list1[k]
    return 1  # not done yet


def pairWiseSum(l11,l22):
# produce a list of ordered pairs? if input list is length m, and n, then i get mxn pairs
# make sure both l1, and l2 are string, not numbers
    l1 = map(lambda x:str(x),l11)
    l2 = map(lambda x:str(x),l22)
    output = []
    for item1 in l1:
        temp = []
        for item2 in l2:
            a=item1+item2
            temp.append(a)
        output.extend(temp)
    return output


def addString(string1):
# this adds up the digits in a string of numbers;
    count = 0
    for item in string1:
        count = count + int(item)
    return count

def main():
    numberPool = [1,2,3,4]
    numberOfOperation = 3
    goal = 8

    comp = [numberPool]*(numberOfOperation+1)
    
    temp = comp[0]
    for i in range(1,len(comp)):
        temp = pairWiseSum(temp,comp[i])
    

    sumz = map(lambda x: (x,addString(x)),temp)
    match = []
    for item in sumz:
        if item[1] == goal:
            match.append(item[0])

    return match




# there are k different base situations, k = length of numberPool
# number of ways to get to 5 is number of ways to get to 4, number of ways to get to 3* number of ways to get to 2

# so if k = 10, we have to find number of ways to get to 1,2,3,4,5,6,7,8,9. Then
# 1*9 + 2*8 + 3*7 + 4*6 + 5*5   where 1 is Number of ways to get 1, 2 is number of ways to get 2 etc...

# so i want to use a dynamic programming approach, and save all the results along the way to get to 9
