

## Note:

#~~~~~~~~~~~~~
#for VIM
#to quit:
#esc  --> to exit the insert mode
#press :   to enter command
#press wq!   to save and quit


# for git:  steps to commit local files to remote server:
# if you dont have a repo initialized:
# git remote add origin "https://github.com/myName/myRepositoryName"

# then the usual thing:
# git add
# git commit -m "commit message"
# git push origin master


#~~~~~


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



# xvalidation function that takes in a full dataframe... label/Y, xvar1, xvar2, xvar3, xvar4... and divide into
# some % of training and test. user can also specify number times to loop through
# the one i have here is for a classification tree, but i think we can replace the function with something else
# returns a count on the number of correct predictions
# the 1st one is faster


def xValidate(trainSet,prop, loop1):
    import numpy as np
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    # turn train into two subsets: train and test
    # prop is the proportion of test set
    n = len(trainSet)
    test1Size = int(prop*n)
    names = list(trainSet.columns[1:len(trainSet.columns)])
    YName = trainSet.columns[0]
    # randomize the data using the reindex function from numpy
    
    record = []
    for j in range(loop1):
        print "starting loop" + str(j+1)
        
        trainNew = trainSet.reindex(np.random.permutation(trainSet.index))
        Y = trainNew[:-test1Size:][YName]
        X = trainNew[:-test1Size:][names]
        
        Ycheck = list(trainNew[:test1Size:][YName])
        Xcheck = trainNew[:test1Size:][names]
        
        dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
        dt.fit(X, Y)
        pred = list(dt.predict(Xcheck))
        
        count = 0
        
        if test1Size != len(pred):
            print "Length of prediction is not same as specified size"
        
        for i in range(test1Size):
            if int(pred[i]) == int(Ycheck[i]):
                count = count + 1
        
        record.append(count)


    return record

#~~~~~~~~~~~~~~~~~~~~~~~~~

def xValidate2(trainSet,prop, loop1):
    from sklearn.tree import DecisionTreeClassifier, export_graphviz
    import numpy as np
    import pandas as pd

    # turn train into two subsets: train and test
    # prop is the proportion of test set
    n = len(trainSet)
    test1Size = int(prop*n)
    names = list(trainSet.columns[1:len(trainSet.columns)])
    YName = trainSet.columns[0]
    # randomize the data using the reindex function from numpy
    
    record = []
    for j in range(loop1):
        
        print "starting loop" + str(j+1)
        
        newInd = np.random.permutation(trainSet.index)
        testInd = newInd[0:test1Size]
        trainInd = newInd[test1Size:len(newInd)]
        
        Y = trainSet.loc[trainInd][YName]
        X = trainSet.loc[trainInd][names]
        
        Ycheck = list(trainSet.loc[testInd][YName])
        Xcheck = trainSet.loc[testInd][names]
        
        dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
        dt.fit(X, Y)
        pred = list(dt.predict(Xcheck))
        
        count = 0
        
        if test1Size != len(pred):
            print "Length of prediction is not same as specified size"
        
        for i in range(test1Size):
            if int(pred[i]) == int(Ycheck[i]):
                count = count + 1
        
        record.append(count)
    
    
    return record





def findDistance(ar1,ar2):
    count = 0
    for i in range(len(ar1)):
        count = count + abs(int(ar1[i]) - int(ar2[i]))
    return count


def digitKNN(trainList,inputSet):
    
    from collections import Counter
    
    
    n = len(trainSet)
    test1Size = int(prop*n)
    
    ranInd = np.random.permutation(range(n))
    testInd = ranInd[0:test1Size]
    trainInd = ranInd[test1Size:n]
    
    X = []
    for item in trainInd:
        X.append(trainSet[item])
    #X = trainNew[:-test1Size:][names]
    result = []
    for item1 in inputSet:
        tempDis = map(lambda x:findDistance(x,item1),X)
        cutoff = 2*sorted(tempDis)[3]
        tempVote = []
        for i in range(test1Size):
            if tempDis[i] < cutoff:
                tempVote.append(Ycheck[i])
        data = Counter(tempVote)
        result.append(data.most_common()[0])
    
    result2 = []
    for item in result:
        result2.append(item[0])
    return result2
