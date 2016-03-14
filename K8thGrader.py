# this is the code for kaggle's are you smarter than an 8th grader question


# i will scrape outside data...

# first, let's see what kind of questions we have
import csv


def readCSV(fileName,delim):
    # Need csv module
    # delim is delimiter, and quoting is set to none. It has something to do with escape character. Not sure what that means
    # identation  =  4 spaces
    newFile = []
    with open(fileName,'rb') as f:
        reader = csv.reader(f,delimiter=delim)
        for row in reader:
            newFile.append(row)
    return newFile


#readCSV('./../Kaggle8Grader/training_set.tsv','/t')
readCSV('training_set.tsv','\t')


# it looks like with the right text, a text that contains all the info.
# we can do a occurance test. the one with the most co-occurance will most likely be the answer.
# the problem is, how do I find the text of everything.
# if i can't find it, how do i work with the existing text/corpus

