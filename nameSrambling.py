# read in the name folders:
import random
import re

def readCSV(fileName,delim):
    import csv
    # Need csv module
    # delim is delimiter, and quoting is set to none. It has something to do with escape character. Not sure what that means
    # identation  =  4 spaces
    newFile = []
    with open(fileName,'rb') as f:
        reader = csv.reader(f,delimiter=delim)
        for row in reader:
            newFile.append(row)
    return newFile


def generateName(firstN,lastN):  # the inputs are firstnameList, and lastnameList
    fLength = len(firstN)
    lLength = len(lastN)
    fIndex = random.randint(0,fLength-1)
    lIndex = random.randint(0,lLength-1)
    return firstN[fIndex]+' '+lastN[lIndex]
# this does a simple first and last name string and put them together


def stringVowels(NameStr1):
# i want to now extract all substring with the following format:
# starts with consanant, and ends with vowel:
# example: Lisa   will give 2 terms:   Li, and sa
    NameStr = NameStr1.lower()
    vowel = ['a','e','i','o','u']
    consec_re = re.compile(r'^[bcdfghjklmnpqrstvwxz]+[aeiou]{1,2}')
    result = []
    match1 = 3
# this regular expression finds anything start with a string of consanant and ends with 1 or 2 vowels.
    for i in range(len(NameStr)):
        g=consec_re.match(NameStr)
        try:
            match1 = g.group(0)  # this will make sure i find the first match
            NameStr = NameStr.replace(match1,'')
            result.append(match1)
        except AttributeError:
            match1 = 2
    return result
# now i want to remove the match and run it again on the same string until no match found





def main():

    maleFirst = readCSV('dist.male.first.txt','\t')
    Last = readCSV('dist.all.last.txt','\t')
    femaleFirst = readCSV('census-dist-female-first.txt','\t')

    #~~~~~~~~~~~~~~

    # break the names
    FFirst = map(lambda x:x[0].split()[0], femaleFirst)
    MFirst = map(lambda x:x[0].split()[0], maleFirst)

    CFirst = FFirst+MFirst
    LLast = map(lambda x:x[0].split()[0], Last)

    newName = generateName(CFirst,LLast)
    print newName

#~~~~~~~ up next we have vowel extraction;

    lastNameV=map(lambda x:stringVowels(x),LLast)
    firstNameV =map(lambda x:stringVowels(x),CFirst)   # takes a while tho. need a way to optimize the extraction code

# then i can put those together however way i want to do it.  TBC





if __name__ == "__main__":
    main()
